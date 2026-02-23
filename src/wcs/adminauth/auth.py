from AccessControl import Unauthorized
from Acquisition import aq_inner
from Acquisition import aq_parent
from cas import CASClient
from logging import getLogger
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.PluggableAuthService.interfaces.authservice import IPluggableAuthService
from Products.PluggableAuthService.interfaces.plugins import ICredentialsUpdatePlugin
from random import SystemRandom
from urllib.parse import quote
from wcs.adminauth.session import SessionPlugin
from xml.etree.ElementTree import ParseError

import os
import string


SESSION_PLUGIN_METATYPES = [
    "Plone Session Plugin",
    "wcs.adminauth Session Plugin",
]

logger = getLogger("wcs.adminauth")


class AuthenticationView(BrowserView):
    def __init__(self, browser, request):
        super().__init__(browser, request)
        self.cas_server_url = os.environ.get("ADMIN_AUTH_CAS_SERVER_URL", None)
        self.cas_client = CASClient(
            version=3, service_url=self.service_url(), server_url=self.cas_server_url
        )
        self.adminuser = os.environ.get("ADMIN_AUTH_USERID", "admin")

    def __call__(self):
        if "ticket" in self.request.form:
            cas_userid = self.validate_ticket(self.request.form["ticket"])
            if not cas_userid:
                raise Unauthorized("Authentication failed.")

            userid = self.request.form.get("userid", self.adminuser)
            uf = self.find_userfolder(userid)
            if not uf:
                logger.info(f"Authentication failed: User '{userid}' not found.")
            else:
                # Setup session
                uf.updateCredentials(self.request, self.request.response, userid, "")
                logger.info(f"Authenticated '{cas_userid}' as '{userid}'.")

            self.request.response.redirect(self.context.absolute_url())
        else:
            self.request.response.redirect(
                f"{self.cas_server_url}login?service={self.service_url()}"
            )

    def validate_ticket(self, ticket):
        try:
            cas_userid, _attributes, _pgtiou = self.cas_client.verify_ticket(ticket)
            return cas_userid
        except ParseError:
            return None

    def find_userfolder(self, userid):
        """Try to find a user folder with the given userid."""
        uf_parent = aq_inner(self.context)
        info = None

        while not info:
            uf = self.pas_userfolder(uf_parent)
            if uf:
                info = uf._verifyUser(uf.plugins, login=userid)
            if uf_parent is self.context.getPhysicalRoot():
                break
            uf_parent = aq_parent(uf_parent)

        if info:
            return uf
        return None

    def pas_userfolder(self, context):
        """Return a PAS userfolder for the given context and make sure it has
        a session plugin."""
        uf = getToolByName(context, "acl_users")
        # Migrate to PluggableAuthService if needed
        if not IPluggableAuthService.providedBy(uf):
            from Products.PlonePAS.setuphandlers import migrate_root_uf

            migrate_root_uf(context)
            uf = getToolByName(context, "acl_users")

        # If we still don't have a PAS userfolder there's nothing we can do
        if not IPluggableAuthService.providedBy(uf):
            return None

        # Make sure we have a session plugin
        have_session_plugin = False
        plugins = uf._getOb("plugins")
        cred_updaters = plugins.listPlugins(ICredentialsUpdatePlugin)
        for _updater_id, updater in cred_updaters:
            if updater.meta_type in SESSION_PLUGIN_METATYPES:
                have_session_plugin = True
        if not have_session_plugin:
            # Install our session plugin
            plugin = SessionPlugin("session_adminauth")
            uf._setObject(plugin.getId(), plugin)
            plugin = uf["session_adminauth"]
            plugin.manage_activateInterfaces([
                "IAuthenticationPlugin",
                "ICredentialsResetPlugin",
                "ICredentialsUpdatePlugin",
                "IExtractionPlugin",
            ])
            # Set random adminuser password
            # We no longer want to login using a password.
            user_manager = uf.get("users", None)

            random = SystemRandom()
            chars = string.ascii_letters + string.digits
            pw = "".join(random.choice(chars) for i in range(32))

            if user_manager and self.adminuser in user_manager._user_passwords:
                random = SystemRandom()
                chars = string.ascii_letters + string.digits
                pw = "".join(random.choice(chars) for i in range(32))
                user_manager.updateUserPassword(self.adminuser, pw)

        return uf

    def service_url(self):
        url = self.request.getURL()
        if "userid" in self.request.form:
            url += quote("?userid={}".format(self.request.form.get("userid")))
        return url

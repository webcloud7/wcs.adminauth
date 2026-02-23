__version__ = "2.0.0"

from AccessControl.Permissions import add_user_folders
from Products.PluggableAuthService.PluggableAuthService import registerMultiPlugin
from wcs.adminauth import session


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    registerMultiPlugin(session.SessionPlugin.meta_type)
    context.registerClass(
        session.SessionPlugin,
        permission=add_user_folders,
        constructors=(session.manage_addSessionPlugin, session.addSessionPlugin),
        visibility=None,
    )

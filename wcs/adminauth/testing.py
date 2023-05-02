from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig
import os


class AdminauthLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="plone.autoinclude" file="meta.zcml" />'
            '  <autoIncludePlugins target="plone" />'
            '  <autoIncludePluginsOverrides target="plone" />'
            '</configure>',
            context=configurationContext)


        z2.installProduct(app, 'wcs.adminauth')

WCS_ADMINAUTH_FIXTURE = AdminauthLayer()
WCS_ADMINAUTH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(WCS_ADMINAUTH_FIXTURE,), name="wcs.adminauth:Functional")

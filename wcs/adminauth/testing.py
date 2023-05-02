from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
import wcs.adminauth


class AdminauthLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        super(AdminauthLayer, self).setUpZope(app, configurationContext)
        self.loadZCML(package=wcs.adminauth)
        z2.installProduct(app, 'wcs.adminauth')


WCS_ADMINAUTH_FIXTURE = AdminauthLayer()
WCS_ADMINAUTH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(WCS_ADMINAUTH_FIXTURE,), name="wcs.adminauth:Functional")

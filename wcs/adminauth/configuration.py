from App.config import getConfiguration


def get_config():
    config = dict(
        cas_server_url='https://webcloud7.casdoor.com/cas/webcloud7_cas/webcloud7_adminauth/',
    )
    product_configs = getattr(getConfiguration(), 'product_config', dict())
    config.update(product_configs.get('wcs.adminauth', dict()))
    return config

from App.config import getConfiguration


def get_config():
    config = dict(
        cas_server_url='http://localhost:8000/cas/webcloud7/webcoud7_cas/',
    )
    product_configs = getattr(getConfiguration(), 'product_config', dict())
    config.update(product_configs.get('wcs.adminauth', dict()))
    return config

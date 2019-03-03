from tests.helpers import logger
import requests
import config

siteconfiguration_url = config.base_url + '/api/v2/siteconfiguration/1/'

def get_siteconfiguration(auth_token):
    logger.logg("About to call config")
    json_site_config = requests.get(siteconfiguration_url, headers={'Authorization': 'JWT {}'.format(auth_token)}).json()
    logger.logg("Config retrieved")
    return json_site_config

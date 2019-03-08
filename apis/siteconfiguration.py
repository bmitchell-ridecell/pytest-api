import requests
from configs import config

siteconfiguration_url = config.get('base_url') + '/api/v2/siteconfiguration/1/'


def get_siteconfiguration(auth_token):
    json_site_config = requests.get(siteconfiguration_url, headers={'Authorization': 'JWT {}'.format(auth_token)}).json()
    return json_site_config

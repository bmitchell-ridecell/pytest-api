import os
import requests
import json
import hashlib
import sys
import http.client as http_client
from tests.helpers import api_request_helper
from tests.helpers import logger
from tests.apis import authenticate

########################################################################
#
#   Feature:  A admin user only API can retrieve site configuration
#
########################################################################

# Configs
#####################################################
envs = {'eiffel_qa': {'base_url': 'https://eiffel-qa.ridecell.us', 'username': 'dispatcher@ridecell.com',
                      'password_key': 'crj4RN79DebuSJQ515Xv', 'slack_channel': 'DD4G3J3LL'},
        'darwin_qa': {'base_url': 'https://darwin-qa.ridecell.us', 'username': 'dispatcher@ridecell.com',
                      'password_key': '15QKyYnrRkOQt2jqPvS7', 'slack_channel': 'DD4G3J3LL'}}


###################################################################

def test_admin_gets_site_config():

    env_name = "eiffel_qa"

    # Set environment variables from the env_name arg passed into the script
    #####################################################
    base_url = envs[env_name]['base_url']
    username = envs[env_name]['username']
    password = envs[env_name]['password_key']

    config_url = base_url + '/api/v2/siteconfiguration/1/'
    authenticate_url = base_url + '/api/v2/authenticate/'
    last_known_json_path = 'last_known_config/' + env_name + '.json'

    auth_token = authenticate.post_auth_token(username, password, authenticate_url)


    # GET Site Config
    ####################################################
    logger.logg("About to call config")
    json_site_config = requests.get(config_url, headers={'Authorization': 'JWT {}'.format(auth_token)}).json()
    logger.logg("Config retrieved")

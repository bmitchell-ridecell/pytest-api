import os
import requests
import json
import hashlib
import os.path
import sys
import logging
from tests.helpers import api_request_helper

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client

########################################################################
#
#   About:  This is a utility script designed to detect changes in
#           siteconfiguration on the summon platform and notify
#           a Slack channel about what was changed. It needs
#           to be configu for each environment it will monitor as
#           below in the Configs section.
#
#   Setup:  Important secrets are expected in the
#           system env:
#
#           SLACK_API_KEY (from slack web, an api key for slack access)
#           DISPATCH_PASSWORD_EIFFEL_QA   (dispatcher passwored for eiffel qa)
#           DISPATCH_PASSWORD_DARWIN_QA   (dispatcher password for darwin qa)
#
########################################################################

# Configs
#####################################################
envs = {'eiffel_qa': {'base_url': 'https://eiffel-qa.ridecell.us', 'username': 'dispatcher@ridecell.com',
                      'password_key': 'crj4RN79DebuSJQ515Xv', 'slack_channel': 'DD4G3J3LL'},
        'darwin_qa': {'base_url': 'https://darwin-qa.ridecell.us', 'username': 'dispatcher@ridecell.com',
                      'password_key': '15QKyYnrRkOQt2jqPvS7', 'slack_channel': 'DD4G3J3LL'}}


###################################################################

def logg(output):
    print(output)

def test_get_site_config():
    logging.basicConfig()
    # Enable HTTP debugging
    http_client.HTTPConnection.debuglevel = 1

    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    env_name = "eiffel_qa"

    # Set environment variables from the env_name arg passed into the script
    #####################################################
    base_url = envs[env_name]['base_url']
    username = envs[env_name]['username']
    password = envs[env_name]['password_key']

    config_url = base_url + '/api/v2/siteconfiguration/1/'
    authenticate_url = base_url + '/api/v2/authenticate/'
    last_known_json_path = 'last_known_config/' + env_name + '.json'

    # POST Auth Token
    ####################################################
    logg("About to call auth")
    values = {'password': password,
              'username': username}
    response = requests.post(authenticate_url, data=values).json()
    auth_token = response['auth_token']
    logg("Auth complete")

    # GET Site Config
    ####################################################
    logg("About to call config")
    json_site_config = requests.get(config_url, headers={'Authorization': 'JWT {}'.format(auth_token)}).json()
    logg("Config retrieved")

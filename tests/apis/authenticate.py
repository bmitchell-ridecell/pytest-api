from tests.helpers import logger
import requests
import config


authenticate_url = config.get('base_url') + '/api/v2/authenticate/'


def auth_token(username, password):
    response = post_authenticate(username, password)
    return response.json()['auth_token']


def post_authenticate(username, password):
    values = {'password': password,
              'username': username}
    response = requests.post(authenticate_url, data=values)
    logger.logg("Auth complete, status code: " + str(response.status_code))
    return response

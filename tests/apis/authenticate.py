from tests.helpers import logger
import requests

def post_auth_token(username, password, authenticate_url):
    logger.logg("About to call auth")
    values = {'password': password,
              'username': username}
    response = requests.post(authenticate_url, data=values).json()
    auth_token = response['auth_token']
    logger.logg("Auth complete")
    return auth_token

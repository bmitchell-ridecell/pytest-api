from loggings import logger
import requests
from configs import config

authenticate_url = config.get('base_url') + '/api/v2/authenticate/'


def auth_token(customer):
    response = post_authenticate(customer.username, customer.password)
    auth_token = response.json()['auth_token']
    assert auth_token is not None
    customer.auth_token = auth_token
    return customer


def post_authenticate(username, password):
    values = {'password': password,
              'username': username}
    response = requests.post(authenticate_url, data=values)
    logger.logg("Auth complete, status code: " + str(response.status_code))
    return response

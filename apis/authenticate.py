from loggings import logger
import requests
from configs import config

authenticate_url = config.get('base_url') + '/api/v2/authenticate/'


def auth_token(customer):
    response = post_authenticate(customer.username, customer.password)
    return response


def post_authenticate(username, password):
    values = {'password': password,
              'username': username}
    response = requests.post(authenticate_url, data=values)
    logger.logg("Auth complete, status code: " + str(response.status_code))
    return response

from loggings import logger
import requests
from configs import config


def accept_tos_url_for_customer(customer_id):
    return config.get('base_url') + '/api/v2/carsharingcustomers/' + str(customer_id) + '/accept_terms_of_service'


def post_accept_tos(customer_id, auth_token):
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    response = requests.post(accept_tos_url_for_customer(customer_id), headers=jwt_headers)
    logger.logg("Accept ToS status code is : " + str(response.status_code))
    logger.logg(response.json())
    return response


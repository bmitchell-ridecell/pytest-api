from loggings import logger
import requests
from configs import config


def post_accept_tos(customer):
    accept_tos_url_for_customer = config.get('base_url') + '/api/v2/carsharingcustomers/' + str(customer.customer_id) + '/accept_terms_of_service'
    jwt_headers = {'Authorization': 'JWT {}'.format(customer.auth_token)}

    response = requests.post(accept_tos_url_for_customer, headers=jwt_headers)
    assert response.status_code == 200
    logger.logg("Accept ToS status code is : " + str(response.status_code))
    logger.logg(response.json())

    return customer


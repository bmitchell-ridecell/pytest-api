from loggings import logger
import requests
import config


address_defaults = {"lat":0,
                    "lng":0,
                    "display_name":"780 Oak Grove Rd , Concord, CA 94518"}


def address_url_for_customer(customer_id):
    return config.get('base_url') + '/api/v2/carsharingcustomers/' + str(customer_id) + '/mailing_address'


def post_address(customer_id, auth_token):
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    response = requests.post(address_url_for_customer(customer_id), data=address_defaults, headers=jwt_headers)
    logger.logg("Post address status code: " + str(response.status_code))
    logger.logg(response.json())
    return response

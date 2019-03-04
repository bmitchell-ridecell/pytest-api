from tests.helpers import logger
import requests
import config
import random


def post_random_drivers_license(customer_id, auth_token):
    drivers_licens_url = drivers_license_url_for_customer(customer_id)
    values = {"date_of_birth":"1985-05-08","license_expiry_date":"2022-04-05","license_issued_state":"California","license_number":random_drivers_license()}
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    response = requests.post(drivers_licens_url, data=values, headers=jwt_headers)
    return response


def drivers_license_url_for_customer(customer_id):
    return config.get('base_url') + '/api/v2/carsharingcustomers/' + str(customer_id) + '/driver_license'


def random_drivers_license():
    return config.rand_x_digit_num(10, False)

from tests.helpers import logger
import requests
import config
import random

carsharingcustomers_url = config.get('base_url') + '/api/v2/carsharingcustomers'


def post_carsharingcustomer(email, password, phone_number):
    values = {'email': email,
              'password': password,
              'phone_number': phone_number}
    response = requests.post(carsharingcustomers_url, data=values)
    logger.logg("POST carsharingcustomers complete, status code: " + str(response.status_code))
    return response


def post_random_carsharingcustomer():
    email = "brad+pytest"+rand_x_digit_num(5)+"@ridecell.com",
    password = config.get('default_password')
    phone_number = rand_x_digit_num(10, False)
    response = post_carsharingcustomer(email, password, phone_number)
    return response


def rand_x_digit_num(x, leading_zeroes=True):
    """Return an X digit number, leading_zeroes returns a string, otherwise int"""
    if not leading_zeroes:
        # wrap with str() for uniform results
        return random.randint(10**(x-1), 10**x-1)
    else:
        if x > 6000:
            return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
        else:
            return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)


def patch_carsharingcustomer(customer_id, auth_token, first_name, last_name, pin_number):
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    values = {"first_name": first_name,
              "last_name": last_name,
              "pin_number": pin_number}
    response = requests.patch(carsharingcustomers_url+"/"+str(customer_id), data=values, headers=jwt_headers)
    logger.logg("PATCH carsharingcustomers complete, status code: " + str(response.status_code))
    return response





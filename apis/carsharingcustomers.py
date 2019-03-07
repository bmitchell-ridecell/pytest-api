from loggings import logger
import requests
import config


carsharingcustomers_url = config.get('base_url') + '/api/v2/carsharingcustomers'


def post_carsharingcustomer(email, password, phone_number):
    values = {'email': email,
              'password': password,
              'phone_number': phone_number}
    response = requests.post(carsharingcustomers_url, data=values)
    logger.logg("POST carsharingcustomers complete, status code: " + str(response.status_code))
    return response


def post_random_carsharingcustomer():
    email = "brad+pytest"+config.rand_x_digit_num(5)+"@ridecell.com",
    password = config.get('default_password')
    phone_number = config.rand_x_digit_num(10, False)
    response = post_carsharingcustomer(email, password, phone_number)
    return response


def patch_carsharingcustomer(customer_id, auth_token, first_name, last_name, pin_number):
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    values = {"first_name": first_name,
              "last_name": last_name,
              "pin_number": pin_number}
    response = requests.patch(carsharingcustomers_url+"/"+str(customer_id), data=values, headers=jwt_headers)
    logger.logg("PATCH carsharingcustomers complete, status code: " + str(response.status_code))
    return response

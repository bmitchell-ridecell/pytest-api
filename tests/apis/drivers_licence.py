import requests
import config


dl_defaults = {"date_of_birth": "1985-05-08",
               "license_expiry_date": "2022-04-05",
               "license_issued_state": "California"}


def drivers_license_url_for_customer(customer_id):
    return config.get('base_url') + '/api/v2/carsharingcustomers/' + str(customer_id) + '/driver_license'


def post_random_drivers_license(customer_id, auth_token):
    drivers_license_url = drivers_license_url_for_customer(customer_id)
    values = {"date_of_birth": dl_defaults['date_of_birth'],
              "license_expiry_date": dl_defaults['license_expiry_date'],
              "license_issued_state": dl_defaults['license_issued_state'],
              "license_number": random_drivers_license()}
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    response = requests.post(drivers_license_url, data=values, headers=jwt_headers)
    return response


def put_drivers_license_verified(customer_id, auth_token, license_num):
    drivers_license_url = drivers_license_url_for_customer(customer_id)
    values = {"date_of_birth": dl_defaults['date_of_birth'],
              "license_expiry_date": dl_defaults['license_expiry_date'],
              "license_issued_state": dl_defaults['license_issued_state'],
              "license_number": license_num,
              "is_license_verified": True}
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    response = requests.post(drivers_license_url, data=values, headers=jwt_headers)
    return response


def random_drivers_license():
    return config.rand_x_digit_num(10, False)

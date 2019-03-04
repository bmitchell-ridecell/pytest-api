from tests.apis import authenticate
from tests.apis import carsharingcustomers
from tests.apis import cards
from tests.apis import drivers_licence

import config
import requests

###############################################################################
#
#   Feature:  Simulate mobile application flow for creating carsharingcustomer
#
###############################################################################


def test_create_carsharing_customer_MIV_express_us():

    response = carsharingcustomers.post_random_carsharingcustomer()
    print(response.json())
    customer_id = response.json()['id']
    username = response.json()['user']['username']
    password = config.get('default_password')

    auth_token = authenticate.auth_token(username, password)
    assert auth_token is not None

    response = carsharingcustomers.patch_carsharingcustomer(customer_id, auth_token, "Fred", "Smith", "")
    assert response.status_code == 200

    response = cards.post_fake_stripe_card(customer_id, auth_token)
    assert response.status_code == 201

    response = drivers_licence.post_random_drivers_license(customer_id, auth_token)
    assert response.status_code == 200
    print(response.json())
    assert int(response.json()['license']['license_number']) > 0


















from tests.apis import authenticate
from tests.apis import carsharingcustomers
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













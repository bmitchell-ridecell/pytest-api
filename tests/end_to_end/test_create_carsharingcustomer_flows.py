from apis import address, accept_terms_of_service, authenticate, carsharingcustomers, miv_document_specifications, \
    cards, drivers_licence
from configs import config


###############################################################################
#
#   Feature:  Massiv app api flow simulation for creating carsharingcustomer
#             with Manual Identity Verification (MIV) image uploads
#             and Dispatcher approval from Ops Center
#
###############################################################################


def test_create_carsharing_customer_MIV_express_us():

    # POST carsharing customer
    response = carsharingcustomers.post_random_carsharingcustomer()
    print(response.json())
    customer_id = response.json()['id']
    username = response.json()['user']['username']
    password = config.get('default_password')

    # Get auth token
    auth_token = authenticate.auth_token(username, password)
    assert auth_token is not None

    # Add first, last name
    response = carsharingcustomers.patch_carsharingcustomer(customer_id, auth_token, "Fred", "Smith", "")
    assert response.status_code == 200

    # Add credit card
    response = cards.post_fake_stripe_card(customer_id, auth_token)
    assert response.status_code == 201

    # Add drivers license
    response = drivers_licence.post_random_drivers_license(customer_id, auth_token)
    assert response.status_code == 200
    print(response.json())
    assert int(response.json()['license']['license_number']) > 0
    assert int(response.json()['license']['is_license_verified']) == 0
    drivers_license_num = int(response.json()['license']['license_number'])

    # PUT license verified
    response = drivers_licence.put_drivers_license_verified(customer_id, auth_token, drivers_license_num)
    print(response.json())
    assert int(response.json()['license']['is_license_verified']) == 1
    # TODO does/should this require admin user auth token?

    # POST Address
    response = address.post_address(customer_id, auth_token)
    assert response.status_code == 200

    # POST Accept ToS
    response = accept_terms_of_service.post_accept_tos(customer_id, auth_token)
    assert response.status_code == 200

    # GET MiV doc specifications
    response = miv_document_specifications.get_miv_document_specifications(auth_token)
    assert response.status_code == 200
    print(response.json())

    # POST MiV docs




















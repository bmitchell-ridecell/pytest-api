from apis import address, accept_terms_of_service, authenticate, carsharingcustomers, miv_document_specifications, \
    cards, drivers_licence
from factories import factory

###############################################################################
#
#   Feature:  Massiv app api flow simulation for creating carsharingcustomer
#             with Manual Identity Verification (MIV) image uploads
#             and Dispatcher approval from Ops Center
#
###############################################################################


def test_create_carsharing_customer_MIV_express_us():

    carsharing_customer = factory.create_random_customer("full_carsharing")
    # POST carsharing customer
    response = carsharingcustomers.post_random_carsharingcustomer(carsharing_customer)
    carsharing_customer.customer_id = response.json()['id']

    # Get auth token
    auth_token = authenticate.auth_token(carsharing_customer)
    assert auth_token is not None
    carsharing_customer.auth_token = auth_token

    carsharing_customer2 = factory.create_random_customer("medium_carsharing")
    # Add first, last name
    response = carsharingcustomers.patch_carsharingcustomer(carsharing_customer, carsharing_customer2)
    assert response.status_code == 200

    # Add credit card
    response = cards.post_fake_stripe_card(carsharing_customer)
    assert response.status_code == 201

    # Add drivers license
    response = drivers_licence.post_random_drivers_license(carsharing_customer)
    assert response.status_code == 200
    print(response.json())
    assert int(response.json()['license']['license_number']) > 0
    assert int(response.json()['license']['is_license_verified']) == 0
    carsharing_customer.driver_license_number = int(response.json()['license']['license_number'])

    # PUT license verified
    response = drivers_licence.put_drivers_license_verified(carsharing_customer)
    print(response.json())
    assert int(response.json()['license']['is_license_verified']) == 1
    # TODO does/should this require admin user auth token?

    # POST Address
    response = address.post_address(carsharing_customer)
    assert response.status_code == 200

    # POST Accept ToS
    response = accept_terms_of_service.post_accept_tos(carsharing_customer)
    assert response.status_code == 200

    # GET MiV doc specifications
    response = miv_document_specifications.get_miv_document_specifications(carsharing_customer)
    assert response.status_code == 200
    print(response.json())

    # POST MiV docs




















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
    carsharing_customer = authenticate.auth_token(carsharing_customer)

    # create random customer2, patch customer with customer2's data
    carsharing_customer2 = factory.create_random_customer("medium_carsharing")
    carsharing_customer = carsharingcustomers.patch_carsharingcustomer(carsharing_customer, carsharing_customer2)

    # Add credit card
    carsharing_customer = cards.post_fake_stripe_card(carsharing_customer)

    # Add drivers license
    carsharing_customer = drivers_licence.post_random_drivers_license(carsharing_customer)

    # PUT license verified
    carsharing_customer = drivers_licence.put_drivers_license_verified(carsharing_customer)

    # TODO does/should this require admin user auth token?

    # POST Address
    carsharing_customer = address.post_address(carsharing_customer)

    # POST Accept ToS
    carsharing_customer = accept_terms_of_service.post_accept_tos(carsharing_customer)

    # GET MiV doc specifications
    response = miv_document_specifications.get_miv_document_specifications(carsharing_customer)
    assert response.status_code == 200




















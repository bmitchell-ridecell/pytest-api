import requests
from configs import config


def post_fake_stripe_card(customer):
    cards_url = config.get('base_url') + '/api/v2/carsharingcustomers/' + str(customer.customer_id) + '/cards'
    values = {"stripe_token": "tok_visa"}
    jwt_headers = {'Authorization': 'JWT {}'.format(customer.auth_token)}
    response = requests.post(cards_url, data=values, headers=jwt_headers)

    return response

from tests.helpers import logger
import requests
import config
import random


def post_fake_stripe_card(customer_id, auth_token):
    card_url = cards_url_for_customer(customer_id)
    values = {"stripe_token": "tok_visa"}
    jwt_headers = {'Authorization': 'JWT {}'.format(auth_token)}
    response = requests.post(card_url, data=values, headers=jwt_headers)
    return response


def cards_url_for_customer(customer_id):
    return config.get('base_url') + '/api/v2/carsharingcustomers/' + str(customer_id) + '/cards'

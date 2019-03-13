from apis import authenticate
from configs import config
from factories import factory


def test_existing_customer_get_auth_token():
    username = config.get('customer_username')
    password = config.get('customer_password')

    response = authenticate.post_authenticate(username, password)
    assert response.status_code == 200


def test_non_user_cannot_get_auth_token():
    random_customer = factory.create_random_customer("carsharing_minimal")
    response = authenticate.post_authenticate(random_customer.username, random_customer.password)
    assert response.status_code == 400


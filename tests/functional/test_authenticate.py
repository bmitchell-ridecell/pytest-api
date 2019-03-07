from apis import authenticate
import config


def test_existing_customer_get_auth_token():
    username = config.get('customer_username')
    password = config.get('customer_password')

    response = authenticate.post_authenticate(username, password)
    assert response.status_code == 200


def test_non_user_cannot_get_auth_token():
    username = "foo"
    password = "barqqqq"

    response = authenticate.post_authenticate(username, password)
    assert response.status_code == 400


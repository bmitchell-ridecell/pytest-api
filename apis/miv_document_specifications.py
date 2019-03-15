import requests
from configs import config

miv_document_specification_url = config.get('base_url') + '/api/v3/manual_identity_verification_document_specifications/'


def get_miv_document_specifications(customer):
    jwt_headers = {'Authorization': 'JWT {}'.format(customer.auth_token)}
    response = requests.get(miv_document_specification_url, headers=jwt_headers)

    return response


from django.test import TestCase

from douban_client import DoubanClient

API_KEY = '0a7e27702d9b9bd41f7a765088d2d37c'
API_SECRET = '12e7950393c30b55'
SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w'
token = '37213e8ef26d4005a563bbacd747c00f'


class Client(DoubanClient):

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)

    def get_authorize_url(self):
        return self.client.authorize_url()


class SimpleTest(TestCase):
    def test_login(self):

        client = Client(API_KEY, API_SECRET, '/', SCOPE)
        #print client.authorize_url
        #code = raw_input('Enter the verification code:')
        #client.auth_with_code(code)
        #client.auth_with_token(token)

        print client.get_authorize_url()
        print client.client.token_url()
        # TODO provide client_id, client_secret, redirect
        #print client.client.get_token()
        client.auth_code.get_token

        #print client.user.me
        #print client.miniblog.home_timeline(100)

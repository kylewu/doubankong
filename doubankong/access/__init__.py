from douban_client import DoubanClient

API_KEY = '0a7e27702d9b9bd41f7a765088d2d37c'
API_SECRET = '12e7950393c30b55'
SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w'

REDIRECT_LINK = 'http://127.0.0.1:8000/callback/'

client = DoubanClient(API_KEY, API_SECRET, REDIRECT_LINK, SCOPE)

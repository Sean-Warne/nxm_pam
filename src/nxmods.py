import json
import requests

BASE_URL = 'https://api.nexusmods.com'

def user_auth(api_key):
    r = requests.get(f'{BASE_URL}/v1/users/validate.json', headers={'accept': 'application/json', 'apikey': api_key})
    print(json.dumps(r.json()))
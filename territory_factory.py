import requests
import json
from pprint import pprint

base_url = 'https://developer-lostark.game.onstove.com'
with open('data/stove_api_key.txt') as f:
    api_key = f.read().strip()

header = {
    'accept': 'application/json',
    'authorization': f'bearer {api_key}',
    'content-Type': 'application/json'
}

body = {
  "Sort": "GRADE",
  "CategoryCode": 50000,
  "ItemName": "오레하",
  "PageNo": 0,
  "SortCondition": "ASC"
}

response = requests.post(url=base_url+'/markets/items',
                        headers= header,
                        json = body)

print(response.status_code)
pprint(response.json())



import re
import requests
import pprint

from pymongo import MongoClient
client = MongoClient()

for i in range(1, 10):
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=17%E5%90%8B%E7%AD%86%E9%9B%BB&page={}&sort=rnk/dc&price=15000-100000'.format(i)
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(i)
        print('error', r.status_code)
        continue

    data = r.json()
    for product in data['prods']:
        client.pchome.products.insert_one(product)

 
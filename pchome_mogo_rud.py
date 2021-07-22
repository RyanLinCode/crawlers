import requests
import pprint

from pymongo import MongoClient
client = MongoClient()
db = client.pchome
coll = db.products

# name contains msi  '$options': 'i'不區分大小寫
name_condition = {'name': {'$regex': '.*Msi.*', '$options': 'i'}}
# data = coll.find(name_condition)

# comparison operator price > 3000
price_condition = {'price': {'$gt': 37000}}
# data = coll.find(price_condition)

# and operator example
# data = coll.find({'$and': [name_condition, price_condition]})
# for d in data:
#     print(d['name'] ,d['price'])

# update operator example
# coll.update_one({'name': 'MSI Creator 15 A10SF-238TW 黑(i7-10875H/16G/1T SSD/RTX2070 8G/15.6UHD/Win10P)創作者筆電'}, {'$set': {'price': 20000}})

# insert if net exist
# upsert example
# coll.update_one({'name' : 'HP測試筆電'}, {'$set': {'name': 'HP測試筆電'}}, upsert=True)

# delete example
coll.delete_one({'name' : 'HP測試筆電'})


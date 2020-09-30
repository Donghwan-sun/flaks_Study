import sys
from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")

mydb = my_client['test']
mycol = mydb['customers']
doc = [{"name": "sundonghwan", "address": "MOKDONG, Seoul"},
       {"name": "KIM", "address": "MOKDONG, Seoul"},
       {"name": "PARK", "address": "MOKDONG, Seoul"}]

x = mycol.insert_many(doc)
print(x.inserted_ids)

fine = mycol.find().sort("name")

for list in fine:
       print(list['name'])
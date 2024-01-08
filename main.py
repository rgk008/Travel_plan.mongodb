import json
from  pymongo.mongo_client import MongoClient

db_uri = "mongodb+srv://rgk008:pilota380@cluster0.4o9zwji.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(db_uri)

db_name = "travel"
col_travel= "travel_plan"

db = client[db_name]

travel = db[col_travel]

file = open("Travel_plan.json","r")
data1 = file.read()
data = json.loads(data1)

for i in data:
    travel.insert.one(i)





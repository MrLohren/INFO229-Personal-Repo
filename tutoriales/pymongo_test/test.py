import pymongo

myclient = pymongo.MongoClient(host="localhost", port=27017)

#new db
db = myclient["test_pymongo"]
collection = db["junk"]

#insert
collection.insert_one({"_id" : "$inc", "name": "joan"})

#find
'''results = collection.find({})
for x in results:
    print(x)'''

#delete
#res = collection.delete_many({})

#update
#collection.update_one({"_id" : 0}, {"$set" :{"new_field" : "sakldja"}})
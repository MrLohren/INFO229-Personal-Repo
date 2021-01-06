import pymongo

myclient = pymongo.MongoClient(host="localhost", port=27017)

#new db
db = myclient["test_pymongo"]
collection = db["junk"]

'''query = "Silla"
content = {
    "info" : "jasdkhja",
    "consultas" : 1
}'''

#insert
'''collection.insert_one({"query" : query,
                       "content" : content
                       })'''

#find
'''results = collection.find({})
for x in results:
    print(x)'''
x = [i for i in collection.find({"query" : "ss"})]
print(x)
#delete
#collection.delete_many({})

#update
#collection.update_one({"_id" : 0}, {"$set" :{"new_field" : "sakldja"}})
#collection.update_one({})
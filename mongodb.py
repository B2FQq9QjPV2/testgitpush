import pymongo

client = pymongo.MongoClient("mongodb+srv://megha:H8hhB2FQq9QjPBV2@cluster0.05juglt.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Megha",
    "Email" : "Megha@gmail",
    "surname" : "wadhwa"
}

db1 = client["mongotest"]
coll = db1['test1']
coll.insert_one(d )
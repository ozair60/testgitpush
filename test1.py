import pymongo

client = pymongo.MongoClient("mongodb+srv://shaikhozair60:Ozair60@cluster0.iqyponp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "Name" : "Ozair",
    "email" : "shaikhozair60@gmail.com",
    "surname" : "Shaikh"
}

d1 = {
    "Name" : "Ozair",
    "email" : "shaikhozair60@gmail.com",
    "surname" : "Shaikh"
}

db1 = client['test1']
coll = db1['test']
coll.insert_one(d)
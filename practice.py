from pymongo import MongoClient
client = MongoClient('mongodb+srv://syahrinvirnanda:syahrin123@cluster0.ar4suzr.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# doc = {'name': 'SyahrinVirnanda', 'age': 16}
# doc2 = {'name': 'naja', 'age': 16}
# doc3 = {'name': 'daus', 'age': 16}

# db.users.insert_one(doc)
# db.users.insert_one(doc2)
# db.users.insert_one(doc3)

# user = db.users.find_one({'name': 'SyahrinVirnanda'})

# print(user)

# db.users.update_one({'name': 'SyahrinVirnanda'}, {'$set': {'age': 17}})

db.users.delete_one({'name': 'SyahrinVirnanda'})
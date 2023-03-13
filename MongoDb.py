import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["pythondb"]
mycol=mydb["users"]
mydict=[
    {"name":"vignesh","age":22},
    {"name":"ajith","age":52},
    {"name":"suresh","age":18},
    {"name":"balaji","age":24}
]
mycol.insert_many(mydict)
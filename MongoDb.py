import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["pythondb"]
mycol=mydb["users"]
mydict=[
    {"name":"vignesh","age":22},
    {"name":"vignesh","age":22},
    {"name":"vignesh","age":22},
    {"name":"vignesh","age":22}
]
mycol.insert_many(mydict)
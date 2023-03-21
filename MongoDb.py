import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
print(myclient.list_database_names(),"\n")
mydb=myclient["pythondb"]
print(mydb.list_collection_names());
print(mydb.name)
mycol=mydb["users"]
mydict=[
    {"name":"vignesh","age":22},
    {"name":"ajith","age":52},
    {"name":"suresh","age":18},
    {"name":"balaji","age":24}
]

print("Single Document: ",mycol.find_one())

for mycol in mycol.find():
    print(mycol['name'])

print(dir(mycol),'\n\n')
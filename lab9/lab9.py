from pymongo import MongoClient

connection_string = "mongosh "mongodb+srv://cluster0.hhlky.mongodb.net/" --apiVersion 1 --username rebeccavannivirginia"
client = MongoClient(connection_string)
db = client["ecn2wh"]

collection = db[FRIENDS]

documents = [
    {"name": "Milly", "age": 19, "city": "Boston"},
    {"name": "Katherine", "age": 19, "city": "Madison"},
    {"name": "Lizzie", "age": 19, "city": "Baltimore"},
    {"name": "Madi", "age": 21, "city": "Charlottesville"},
    {"name": "Alex", "age": 19, "city": "Atlanta"},
]

collection.insert_many(documents)

query_results = collection.find().limit(3)  
for doc in query_results:
    print(doc)

client.close()

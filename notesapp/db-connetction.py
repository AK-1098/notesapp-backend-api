from pymongo import MongoClient # type: ignore

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access a database
db = client["mydatabase"]

# Access a collection
collection = db["mycollection"]

# Insert a document
data = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(data)

# Fetch documents
for document in collection.find():
    print(document)

from pymongo import MongoClient # type: ignore

# Connect to MongoDB
client = MongoClient("mongodb://admin:password123@127.0.0.1:27017/")

# Access the database
db = client["noteapp"]

# Access a collection
collection = db["mycollection"]

# Perform an operation (e.g., insert)
data = {"name": "Alice", "age": 25}
collection.insert_one(data)

print("Data inserted successfully!")

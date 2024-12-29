# File: myapp/utils/mongo_utils.py
from pymongo import MongoClient # type: ignore

def insert_data():
    client = MongoClient("mongodb://admin:password123@127.0.0.1:27017/")
    db = client["noteadd"]
    collection = db["mycollection"]
    data = {"name": "Alice", "age": 25}
    collection.insert_one(data)
    print("Data inserted successfully!")

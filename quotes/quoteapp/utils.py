from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb://localhost")

    db = client.WEBHW10
    return db
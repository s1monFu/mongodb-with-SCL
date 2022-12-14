###
# Author: Simon Fu
# A simple program that creates two clients connecting to mongodb server
#   and access the same document repeatedly
###


import pymongo
import string
import random
import io
from multiprocessing import *


def init_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["customers"]
    dict = {"name": "John", "address": "Highway 37"}
    document = collection.insert_one(dict)
    return client

def read_document():
    print("======READ BEGIN======")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["customers"]
    # find the first document in the collection repeatedly
    for i in range(10):
        document = collection.find_one()
        print(document)
    print("======READ ENDS======")
    
def write_document():
    print("======WRITE BEGIN======")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["customers"]
    # Find the first document in the collection, update it with a randomly generated value
    for i in range(10):
        query = { "name": {"$regex": ".*" }}
        newvalues = { "$set": { "name": f'{random.choice(string.ascii_letters)}{random.randint(0, 99)}' } }
        collection.update_many(query,newvalues)
    print("======WRITE ENDS======")

def report():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    result = db.command("serverStatus")
    return result
if __name__ == '__main__':
    # Connect to local database and create dummy data. 
    # Uncomment this secton first time running the script
    # init_db()

    # Create 2 clients and repeatedly read from the same document
    p1 = Process(target=read_document())
    p2 = Process(target=read_document())

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    result = report()
    f = open("result.txt","w")
    f.write(str(result))
    # Create 2 clients and repeatedly write to the same document
    # p3 = Process(target=write_document())
    # p4 = Process(target=write_document())

    # p3.start()
    # p4.start()

    # p3.join()
    # p4.join()
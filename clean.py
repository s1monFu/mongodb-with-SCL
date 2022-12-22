from pymongo import MongoClient

dbname = "test"
collectname = "testing"

def delete_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client[dbname]
    col = db[collectname]
    col.delete_many({})

def clean_profile():
    client = MongoClient("mongodb://localhost:27017/")
    db = client[dbname]
    db.setProfilingLevel(0)
    db.system.profile.drop()
    db.setProfilingLevel(2)

if __name__ == '__main__':
    delete_data()
    # clean_profile()
    
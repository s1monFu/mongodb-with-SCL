# This Script records the operation usage on three different operations: 
# . insert_one() 
# . 10 clients repeatedly run write operations 10 times at the same time.

# Operations
# Enable system profiling on a database using command
# . db.setProfilingLevel(2)
# Delete the profiling collection
# . db.setProfilingLevel(0)
# . db.system.profile.drop()
# Show profile
# . db.system.profile.find( { ns : 'test.testing' } ).pretty()

from pymongo import MongoClient
import multiprocessing
import csv

dbname = "test"
profile_collection = "system.profile"

queries = [{"op": "insert"}]
fieldnames = ['op','ns','command','ninserted','keysInserted','numYield','locks','flowControl','responseLength','protocol','millis','ts','client','allUsers','user']
def get_profile_collection():
    """Return mongo collection containing profiling records"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client[dbname]
    col = db[profile_collection]
    return col

if __name__ == "__main__":
    # Clear the system profiling

    col = get_profile_collection()
    # for x in col.find({},{ "ns": 'test.testing' }):
    #     print(x)
    query = list(col.find(queries[0]))
    with open('profile.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(query)

    # Show the current collection documents
    # curdb = client[dbname]
    # collection = curdb[collectname]

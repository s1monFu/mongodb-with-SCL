# This Script records the operation usage on three different operations: 
# . insert_one() 
# . 10 clients repeatedly run write operations 10 times at the same time.

# mongosh commands
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


def get_profile_collection():
    """Return mongo collection containing profiling records"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client[dbname]
    col = db[profile_collection]
    return col

def store_profile_general(query: list):
    fieldnames = ['op','ns','command','ninserted','keysInserted','numYield','locks','flowControl','responseLength','protocol','millis','ts','client','allUsers','user']
    with open('profile_general.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(query)

def store_profile_lock(query: list):
    with open('profile_lock.csv','w') as csvfile:
        fieldnames = ['op','ns','ts','ParallelBatchWriterMode','FeatureCompatibilityVersion','ReplicationStateTransition','Global','Database','Collection','Mutex','ts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dic in query:
            lock_dict = dic['locks']
            print(type(lock_dict))
            lock_dict['op'] = dic['op']
            lock_dict['ns'] = dic['ns']
            lock_dict['ts'] = dic['ts']
            writer.writerow(lock_dict)
                

if __name__ == "__main__":
    # Clear the system profiling
    queries = [{"op": "insert"},{'op': 'find'}]
    col = get_profile_collection()
    # for x in col.find({},{ "ns": 'test.testing' }):
    #     print(x)
    for i in range(len(queries)):
        query = list(col.find(queries[0]))
        store_profile_general(query)
        store_profile_lock(query)

    # Show the current collection documents
    # curdb = client[dbname]
    # collection = curdb[collectname]

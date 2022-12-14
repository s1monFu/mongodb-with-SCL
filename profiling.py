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

def insert_profile_general(query: list):
    fieldnames = ['op','ns','command','storage','writeConflicts','ninserted','keysInserted','numYield','locks','flowControl','responseLength','protocol','millis','ts','client','allUsers','user']
    with open('profile_insert_general.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(query)

def insert_profile_lock(query: list):
    with open('profile_insert_lock.csv','w') as csvfile:
        fieldnames = ['op','ns','ts','ParallelBatchWriterMode','FeatureCompatibilityVersion','ReplicationStateTransition','Global','Database','Collection','Mutex','ts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dic in query:
            lock_dict = dic['locks']
            lock_dict['op'] = dic['op']
            lock_dict['ns'] = dic['ns']
            writer.writerow(lock_dict)
                
def find_profile_general(query: list):
    fieldnames = ['op','ns','command','appName','planCacheKey','keysExamined','docsExamined','cursorExhausted','numYield','nreturned','queryHash','queryExecutionEngine','locks','flowControl','responseLength','protocol','millis','planSummary','execStats','ts','client','allUsers','user']
    with open('profile_find_general.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(query)

def find_profile_lock(query: list):
    with open('profile_find_lock.csv','w') as csvfile:
        fieldnames = ['op','ns','ts','FeatureCompatibilityVersion','Global','Mutex','ts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dic in query:
            lock_dict = dic['locks']
            lock_dict['op'] = dic['op']
            lock_dict['ns'] = dic['ns']
            writer.writerow(lock_dict)

if __name__ == "__main__":
    # Clear the system profiling
    queries = [{"op": "insert"},{'op': 'query'}]
    col = get_profile_collection()
    # for x in col.find({}):
    #     print(x)
    # Insert
    query = list(col.find(queries[0]))
    insert_profile_general(query)
    insert_profile_lock(query)

    # Read
    query = list(col.find(queries[1]))
    find_profile_general(query)
    find_profile_lock(query)
    

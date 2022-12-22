# This Script records the operation usage on three different operations: 
# . insert_one() 
# . 10 clients repeatedly run write operations 10 times at the same time.

# Operations
# Enable system profiling on a database using command
# . db.setProfilingLevel(2)
# Delete the profiling collection
# . db.setProfilingLevel(0)
# . db.system.profile.drop()

from pymongo import MongoClient
from pymongo import Connection
import multiprocessing

dbname = "test"
profile_collection = "system.profile"

def get_profile_collection():
    """Return mongo collection containing profiling records"""
    con = Connection()
    db = con[dbname]
    col = db[profile_collection]
    return col

if __name__ == "__main__":
    # Clear the system profiling

    profile = get_profile_collection()
    print(profile)

    # Show the current collection documents
    # curdb = client[dbname]
    # collection = curdb[collectname]

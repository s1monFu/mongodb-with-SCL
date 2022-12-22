# This script is an earilier attempt of monitoring and recording operations on
# . a mongoDB collection. But monitor operations in real time is not realistic
# . This script cannot correctly capture all operations but can be an example for
# . future research

from pymongo import MongoClient
import time
# Connect to the MongoDB instance
client = MongoClient("mongodb://localhost:27017/")

# # Get the "test" database
# db = client["test"]

# Call the db.currentOp() method to display information on all current operations
# result = client.admin.command("currentOp")
# # result = db.command("currentOp({$all: true})")

# f = open(f'result-insert_one.txt',"w")
# f.write(str(result))
# f.close()
# # Get the "test" database
# db = client["test"]

# Call the db.runCommand() method to display information on all current operations
f = open(f'result-insert_one.txt',"w")

# monitor for 10 seconds
start_time = time.time()
seconds = 10
while True:
    current_time = time. time()
    elapsed_time = current_time - start_time
    if elapsed_time > seconds:
        break
    result = client.admin.command("currentOp",{"$all": True,"$maxTimeMS":"500"})
    

    # Loop through the current operations and display information on the insert operations
    for operation in result["inprog"]:
        if operation["op"] == "insert":
            f.write("Insert operation:\n")
            f.write(f'ns:{operation["ns"]}\n')
            f.write(f'client:{operation["client"]}\n')
            f.write(f'locks:{operation["locks"]}\n')
            f.write(f'lockStats:{operation["lockStats"]}\n')
# Get a list of the recently finished insert operations
# recent_ops = db.command("aggregate", "oplog.rs", pipeline=[
#     {"$match": {"op": "insert"}},
#     {"$group": {"_id": None, "recent": {"$max": "$ts"}}}
# ])

# # Loop through the recently finished insert operations
# for operation in recent_ops:
#     # Get the timestamp of the most recent insert operation
#     recent_ts = operation["recent"]
#     # Query the oplog to get the details of the most recent insert operation
#     recent_op = db.oplog.rs.find_one({"ts": recent_ts})
#     # Access information about the operation
#     namespace = recent_op["ns"]
#     client = recent_op["client"]
#     # Print the information to the console
#     print("Recently finished insert operation:")
#     print(f"ns: {namespace}")
#     print(f"client: {client}")
f.close()
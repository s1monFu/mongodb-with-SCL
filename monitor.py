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
    result = client.admin.command("currentOp",{"$all": True})
    

    # Loop through the current operations and display information on the insert operations
    for operation in result["inprog"]:
        if operation["op"] == "insert":
            f.write("Insert operation:\n")
            f.write(f'ns:{operation["ns"]}\n')
            f.write(f'client:{operation["client"]}\n')
            f.write(f'locks:{operation["locks"]}\n')
            f.write(f'lockStats:{operation["lockStats"]}\n')
    cur_time = time.time()

f.close()
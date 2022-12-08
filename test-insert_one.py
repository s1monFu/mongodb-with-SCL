import multiprocessing
from pymongo import MongoClient

def insert_data(process_id):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test"]
    collection = db["users"]

    # Insert a document with the process ID
    collection.insert_one({"process_id": process_id})

if __name__ == "__main__":

    # Create a list of processes
    processes = []

    # Spawn 10 processes to insert data concurrently
    for i in range(10):
        process = multiprocessing.Process(target=insert_data, args=(i,))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()


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
    while True:
        result = client.admin.command({"currentOp": 1})

        # Loop through the current operations and display information on the insert operations
        for operation in result["inprog"]:
            if operation["op"] == "insert":
                print("Insert operation:")
                print("ns:", operation["ns"])
                print("client:", operation["client"])
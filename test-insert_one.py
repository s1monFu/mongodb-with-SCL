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



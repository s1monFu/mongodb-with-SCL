import multiprocessing
from pymongo import MongoClient

dbname = "test"
collectname = "testing"

def find_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client[dbname]
    col = db[collectname]

    # # Insert document with the process ID
    # for i in range(10):

    ##col.insert_one({"process_id": process_id})
    for x in col.find({},{'process_id':'9'}):
        print(x)

if __name__ == "__main__":

    # Create a list of processes
    # processes = []

    # # Spawn 10 processes to insert data concurrently
    # for i in range(10):
    #     process = multiprocessing.Process(target=find_data, args=(i,))
    #     process.start()
    #     processes.append(process)

    # # Wait for all processes to finish
    # for process in processes:
    #     process.join()
    delete_data()



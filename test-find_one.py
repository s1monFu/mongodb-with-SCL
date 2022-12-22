import multiprocessing
from pymongo import MongoClient

dbname = "test"
collectname = "testing"

client = MongoClient("mongodb://localhost:27017/")
db = client[dbname]
col = db[collectname]

def find_data():
    x = col.find_one()

def find_all():
    client = MongoClient("mongodb://localhost:27017/")
    db = client[dbname]
    col = db[collectname]

    x = col.find_one()
    print(x)


if __name__ == "__main__":

    # Create a list of processes
    processes = []

    # Spawn 10 processes to read data concurrently
    for i in range(10):
        process = multiprocessing.Process(target=find_data)
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()



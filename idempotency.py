from prefect import task, flow
from prefect.transactions import transaction


@task
def download_data():
    """Imagine this downloads some data from an API"""
    return "some data"


@task
def write_data(data: str):
    """This writes the data to a file"""
    with open("data.txt", "w") as f:
        f.write(data)


@flow(log_prints=True)
def pipeline():
    with transaction(key="download-and-write-data") as txn:
        if txn.is_committed():
            print("Data file has already been written. Exiting early.")
            return
        data = download_data()
        write_data(data)
        
        

""" 
If you run this flow, it will write data to a file the first time, but it will exit early on subsequent 
runs because the transaction has already been committed.

Giving the transaction a key will cause the transaction to write a record on commit signifying that the 
transaction has completed. The call to txn.is_committed() will return True only if the persisted record exists.
"""


if __name__ == "__main__":
    pipeline()

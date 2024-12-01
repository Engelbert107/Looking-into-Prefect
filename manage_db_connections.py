from prefect import flow, task, concurrency
from myproject import db

@task
def database_query(query):
    # Here we request a single slot on the 'database' concurrency limit. This
    # will block in the case that all of the database connections are in use
    # ensuring that we never exceed the maximum number of database connections.
    with concurrency("database", occupy=1):
        result = db.execute(query)
        return result

@flow
def my_flow():
    queries = ["SELECT * FROM table1", "SELECT * FROM table2", "SELECT * FROM table3"]

    for query in queries:
        database_query.submit(query)

if __name__ == "__main__":
    my_flow()

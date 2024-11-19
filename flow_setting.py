from prefect import flow


@flow(name="My Flow", description="My flow with a name and description", log_prints=True)
def my_flow():
    print("Hello, I'm a flow")


if __name__ == "__main__":
    my_flow()

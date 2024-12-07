from prefect import flow


@flow
def my_flow():
    print("Hello from inside a Docker container!")

if __name__ == "__main__":
    my_flow.deploy(
        name="my-docker-deploy",
        work_pool_name="my_pool",
        image="my-docker-image:latest",
    )

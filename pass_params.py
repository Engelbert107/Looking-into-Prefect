from prefect import flow


@flow
def hello_world(name: str):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    hello_world.deploy(
        name="pass-params-deployment",
        work_pool_name="my-docker-pool",
        parameters=dict(name="Prefect"),
        image="my_registry/my_image:my_image_tag",
    )

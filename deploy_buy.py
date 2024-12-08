from prefect import flow

@flow(log_prints=True)
def buy():
    print("Buying securities")

if __name__ == "__main__":
    buy.deploy(
        name="my-code-baked-into-an-image-deployment",
        work_pool_name="my-docker-pool",
        image="my_registry/my_image:my_image_tag"
    )

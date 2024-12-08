from prefect import flow
from prefect.docker import DockerImage


@flow(log_prints=True)
def buy():
    print("Buying securities")
    
    

if __name__ == "__main__":
    buy.deploy(
        name="my-custom-dockerfile-deployment",
        work_pool_name="my-docker-pool",  # Ensure this pool exists
        image=DockerImage(
            name="my_image",  # Image name
            tag="deploy-guide",           # Image tag
            dockerfile="Dockerfile",       # Dockerfile path 
            build=False                   # Disable building the image
        ),
        push=True  # Set to True if you want to push to a registry
    )
    




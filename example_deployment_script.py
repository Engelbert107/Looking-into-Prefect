from prefect import flow
from prefect.docker import DockerImage

@flow(log_prints=True)            
def my_flow(name: str = "world"):                          
    print(f"Hello {name}! I'm a flow running in a ECS task!") 


if __name__ == "__main__":
    my_flow.deploy(
        name="my-deployment", 
        work_pool_name="my-work-pool",
        image=DockerImage(                                                 
            name="my-repository:latest",
            platform="linux/amd64",
        )                                                                      
    )       

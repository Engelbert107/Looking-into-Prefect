from prefect import flow


@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":
    # creates a deployment and stays running to monitor for work instructions 
    # generated on the server

    hello_world.serve(
        name="my-first-deployment",
        tags=["onboarding", "testing", "tutorial"],
        description="Creates a deployment and stays running to monitor for work instructions generated on the server.",
        version="tutorial/deployments",
        parameters={"goodbye": True},
        pause_on_shutdown=False,
        interval=60
    )

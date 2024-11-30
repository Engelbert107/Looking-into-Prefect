from prefect import flow, task
from prefect.artifacts import create_link_artifact


@task
def my_first_task():
        create_link_artifact(
            key="irregular-data",
            link="https://nyc3.digitaloceanspaces.com/my-bucket-name/highly_variable_data.csv",
            description="## Highly variable data",
        )


@task
def my_second_task():
        create_link_artifact(
            key="irregular-data",
            link="https://nyc3.digitaloceanspaces.com/my-bucket-name/low_pred_data.csv",
            description="# Low prediction accuracy",
        )


@flow
def my_flow():
    my_first_task()
    my_second_task()


if __name__ == "__main__":
    my_flow()

from prefect import flow
from prefect.artifacts import create_link_artifact


@flow
def my_flow():
    create_link_artifact(
        key="my-important-link",
        link="https://www.prefect.io/",
        link_text="Prefect",
    )


if __name__ == "__main__":
    my_flow()

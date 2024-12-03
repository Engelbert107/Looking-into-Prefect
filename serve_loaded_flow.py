from prefect import flow


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/org/repo.git",
        entrypoint="flows.py:my_flow"
    ).serve(name="my-deployment")

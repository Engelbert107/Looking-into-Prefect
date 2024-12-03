from prefect import flow


my_flow = flow.from_source(
    source="https://github.com/PrefectHQ/prefect.git",
    entrypoint="flows/hello_world.py:hello"
)


if __name__ == "__main__":
    my_flow()

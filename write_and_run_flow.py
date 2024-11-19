from prefect import flow

@flow("My flow")
def my_flow() -> str:
    return "Hello, World!"


if __name__ == "__main__":
    print(my_flow)
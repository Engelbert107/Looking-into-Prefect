from prefect import task, flow
from prefect.states import Completed, Failed


@task
def always_fails_task():
    raise ValueError("I fail successfully")


@task
def always_succeeds_task():
    print("I'm fail safe!")
    return "success"


@flow
def always_succeeds_flow():
    x = always_fails_task.submit()
    y = always_succeeds_task.submit()
    if y.result() == "success":
        return Completed(message="I am happy with this result")
    else:
        return Failed(message="How did this happen!?")


if __name__ == "__main__":
    always_succeeds_flow()

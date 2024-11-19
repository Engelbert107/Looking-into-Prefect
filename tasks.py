from prefect import task
from prefect.task_worker import serve # type: ignore


@task
def my_background_task(name: str):
    # Task logic here
    print(f"Hello, {name}!")


if __name__ == "__main__":
    # NOTE: The serve() function accepts multiple tasks. The Task worker 
    # will listen for scheduled task runs for all tasks passed in.
    serve(my_background_task)

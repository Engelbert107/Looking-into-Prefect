from prefect import flow, task
from prefect.task_runners import ThreadPoolTaskRunner
from prefect_dask.task_runners import DaskTaskRunner # type: ignore
import time


@task
def hello_local(name: str):
    time.sleep(2)
    print(f"Hello {name}!")


@flow # implicitly uses the default task runner, ThreadPoolTaskRunner
def concurrent_nested_flow():
    marvin = hello_local.submit("marvin")
    ford = hello_local.submit("ford")
    marvin.wait(), ford.wait()


@task
def hello_dask():
    print("Hello from Dask!")


@flow(task_runner=DaskTaskRunner())
def dask_nested_flow():
    hello_dask.submit().wait()


@flow # implicitly uses the default task runner, ThreadPoolTaskRunner
def parent_flow():
    concurrent_nested_flow()
    dask_nested_flow()


if __name__ == "__main__":
    parent_flow()

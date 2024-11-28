from prefect import task
from prefect.cache_policies import INPUTS
import threading


cache_policy = INPUTS

@task(cache_policy=cache_policy)
def my_task_version_1(x: int):
    print("my_task_version_1 running")
    return x + 42

@task(cache_policy=cache_policy)
def my_task_version_2(x: int):
    print("my_task_version_2 running")
    return x + 43

""" 
Here both tasks will execute in parallel and perform work despite both tasks using the same cache key.
"""

if __name__ == "__main__":
    thread_1 = threading.Thread(target=my_task_version_1, args=(1,))
    thread_2 = threading.Thread(target=my_task_version_2, args=(1,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

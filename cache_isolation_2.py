import threading

from prefect import task
from prefect.cache_policies import INPUTS
from prefect.locking.memory import MemoryLockManager
from prefect.transactions import IsolationLevel

cache_policy = INPUTS.configure(
    isolation_level=IsolationLevel.SERIALIZABLE,
    lock_manager=MemoryLockManager(),
)


@task(cache_policy=cache_policy)
def my_task_version_1(x: int):
    print("my_task_version_1 running")
    return x + 42


@task(cache_policy=cache_policy)
def my_task_version_2(x: int):
    print("my_task_version_2 running")
    return x + 43

# Here only one of the tasks will run and the other will use the cached value.

if __name__ == "__main__":
    thread_1 = threading.Thread(target=my_task_version_1, args=(2,))
    thread_2 = threading.Thread(target=my_task_version_2, args=(2,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

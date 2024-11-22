from prefect import task
from prefect.cache_policies import TASK_SOURCE

import time


@task(cache_policy=TASK_SOURCE)
def my_stateful_task():
    print('sleeping')
    time.sleep(10)
    return 42

my_stateful_task() # sleeps
my_stateful_task() # does not sleep

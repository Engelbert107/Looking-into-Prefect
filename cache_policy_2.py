from prefect import task
from prefect.cache_policies import INPUTS


my_custom_policy = INPUTS - 'debug'

@task(cache_policy=my_custom_policy)
def my_cached_task(x: int, debug: bool = False):
    print('running...')
    return x + 42


my_cached_task(1)
my_cached_task(1, debug=True) # still uses the cache

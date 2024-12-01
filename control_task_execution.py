from prefect import task, flow

@task
def task_a():
    pass

@task
def task_b():
    pass

@task
def task_c():
    pass
    
@task
def task_d():
    pass

@flow
def my_flow():
    a = task_a.submit()
    b = task_b.submit()
    # Wait for task_a and task_b to complete
    c = task_c.submit(wait_for=[a, b])
    # task_d will wait for task_c to complete
    # Note: If waiting for one task it must still be in a list.
    d = task_d(wait_for=[c])

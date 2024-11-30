from prefect import flow, task


@task
def add_one(x):
    return x + 1


""" 
You can also access state objects directly within a flow through the return_state flag
"""

@flow
def my_flow():
    result = add_one(1)
    assert isinstance(result, int) and result == 2

    state = add_one(1, return_state=True)
    assert state.is_completed() is True
    assert state.result() == 2

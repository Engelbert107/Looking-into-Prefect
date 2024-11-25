from prefect import flow
from prefect.flow_runs import pause_flow_run
from prefect.logging import get_run_logger

@flow
def greet_user():
    logger = get_run_logger()

    user = pause_flow_run(wait_for_input=str)

    logger.info(f"Hello, {user}!")

# In this example, the flow run pauses until a user clicks the Resume button in the Prefect UI, enters 
# a name, and submits the form.
if __name__=="__main__":
    greet_user()
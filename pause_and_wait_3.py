from prefect import flow, pause_flow_run
from prefect.logging import get_run_logger
from prefect.input import RunInput

class UserInput(RunInput):
    name: str
    age: int

@flow
async def greet_user():
    logger = get_run_logger()

    user_input = await pause_flow_run(
        wait_for_input=UserInput.with_initial_data(name="anonymous")
    )
    
    # When a user sees the form for this input, the name field contains "anonymous" as the default.

    if user_input.name == "anonymous":
        logger.info("Hello, stranger!")
    else:
        logger.info(f"Hello, {user_input.name}!")
        

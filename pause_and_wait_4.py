from datetime import datetime
from prefect import flow
from prefect.flow_runs import pause_flow_run
from prefect.logging import get_run_logger
from prefect.input import RunInput

# Provide a dynamic, Markdown description that appears in the Prefect UI when the flow run pauses


class UserInput(RunInput):
    name: str
    age: int


@flow
async def greet_user():
    logger = get_run_logger()
    current_date = datetime.now().strftime("%B %d, %Y")

    description_md = f"""
**Welcome to the User Greeting Flow!**
Today's Date: {current_date}

Please enter your details below:
- **Name**: What should we call you?
- **Age**: Just a number, nothing more.
"""

    user_input = await pause_flow_run(
        wait_for_input=UserInput.with_initial_data(
            description=description_md, name="anonymous"
        )
    )

    if user_input.name == "anonymous":
        logger.info("Hello, stranger!")
    else:
        logger.info(f"Hello, {user_input.name}!")


from prefect import flow
from prefect.input.run_input import receive_input


@flow
async def greeter_flow():
    async for name_input in receive_input(str, timeout=None):
        # Prints "Hello, andrew!" if another flow sent "andrew"
        print(f"Hello, {name_input}!")


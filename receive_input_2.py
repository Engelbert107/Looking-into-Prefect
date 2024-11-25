from prefect import flow
from prefect.input.run_input import receive_input


@flow
async def greeter_flow():
    async for name_input in receive_input(
        str,
        timeout=None,
        with_metadata=True
    ):
        # Input will always be in the field "value" on this object.
        print(f"Hello, {name_input.value}!")


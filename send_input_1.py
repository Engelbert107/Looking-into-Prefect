from prefect import flow, get_client
from prefect.deployments import run_deployment

@flow
async def sender():
    greeter_flow_run = await run_deployment(
        "greeter/send-receive", timeout=0, as_subflow=False
    )
    receiver = receive_input(str, timeout=None, poll_interval=0.1)
    client = get_client()

    while True:
        flow_run = await client.read_flow_run(greeter_flow_run.id)

        if not flow_run.state or not flow_run.state.is_running():
            continue

        name = input("What is your name? ")
        if not name:
            continue

        if name == "q" or name == "quit":
            await send_input(
                EXIT_SIGNAL,
                flow_run_id=greeter_flow_run.id
            )
            print("Goodbye!")
            break

        await send_input(name, flow_run_id=greeter_flow_run.id)
        greeting = await receiver.next()
        print(greeting)

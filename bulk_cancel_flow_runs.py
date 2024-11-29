import anyio


from prefect import get_client
from prefect.client.schemas.filters import FlowRunFilter, FlowRunFilterState, FlowRunFilterStateName
from prefect.client.schemas.objects import StateType



""" 
Use get_clientto set multiple runs to a Cancelled state. 
The code below cancels all flow runs that are in Pending, 
Running, Scheduled, or Late states when the script is run.
"""


async def list_flow_runs_with_states(states: list[str]):
    async with get_client() as client:
        flow_runs = await client.read_flow_runs(
            flow_run_filter=FlowRunFilter(
                state=FlowRunFilterState(
                    name=FlowRunFilterStateName(any_=states)
                )
            )
        )
    return flow_runs


async def cancel_flow_runs(flow_runs):
    async with get_client() as client:
        for idx, flow_run in enumerate(flow_runs):
            print(f"[{idx + 1}] Cancelling flow run '{flow_run.name}' with ID '{flow_run.id}'")
            state_updates = {}
            state_updates.setdefault("name", "Cancelled")
            state_updates.setdefault("type", StateType.CANCELLED)
            state = flow_run.state.copy(update=state_updates)
            await client.set_flow_run_state(flow_run.id, state, force=True)


async def bulk_cancel_flow_runs():
    states = ["Pending", "Running", "Scheduled", "Late"]
    flow_runs = await list_flow_runs_with_states(states)

    while len(flow_runs) > 0:
        print(f"Cancelling {len(flow_runs)} flow runs\n")
        await cancel_flow_runs(flow_runs)
        flow_runs = await list_flow_runs_with_states(states)
    print("Done!")


if __name__ == "__main__":
    anyio.run(bulk_cancel_flow_runs)

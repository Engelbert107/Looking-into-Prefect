import asyncio
from typing import Optional

from prefect import get_client
from prefect.client.schemas.filters import FlowRunFilter
from prefect.client.schemas.objects import FlowRun
from prefect.client.schemas.sorting import FlowRunSort


""" 
This example gets the last three completed flow runs from your workspace.
"""

async def get_most_recent_flow_runs(
    n: int = 3,
    states: Optional[list[str]] = None
) -> list[FlowRun]:
    if not states:
        states = ["COMPLETED"]
    
    async with get_client() as client:
        return await client.read_flow_runs(
            flow_run_filter=FlowRunFilter(
                state={'type': {'any_': states}}
            ),
            sort=FlowRunSort.END_TIME_DESC,
            limit=n,
        )


if __name__ == "__main__":
    last_3_flow_runs: list[FlowRun] = asyncio.run(
        get_most_recent_flow_runs()
    )
    print(last_3_flow_runs)
    
    assert all(
        run.state.is_completed() for run in last_3_flow_runs
    )
    assert (
        end_times := [run.end_time for run in last_3_flow_runs]
    ) == sorted(end_times, reverse=True)

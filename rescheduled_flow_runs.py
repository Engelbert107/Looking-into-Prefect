import asyncio
from datetime import datetime, timedelta, timezone
from typing import Optional


from prefect import get_client
from prefect.client.schemas.filters import (
    DeploymentFilter, FlowRunFilter
)
from prefect.client.schemas.objects import FlowRun
from prefect.client.schemas.sorting import FlowRunSort
from prefect.states import Scheduled

async def reschedule_late_flow_runs(
    deployment_name: str,
    delay: timedelta,
    most_recent_n: int,
    delete_remaining: bool = True,
    states: Optional[list[str]] = None
) -> list[FlowRun]:
    if not states:
        states = ["Late"]

    async with get_client() as client:
        flow_runs = await client.read_flow_runs(
            flow_run_filter=FlowRunFilter(
                state=dict(name=dict(any_=states)),
                expected_start_time=dict(
                    before_=datetime.now(timezone.utc)
                ),
            ),
            deployment_filter=DeploymentFilter(
                name={'like_': deployment_name}
            ),
            sort=FlowRunSort.START_TIME_DESC,
            limit=most_recent_n if not delete_remaining else None
        )

        if not flow_runs:
            print(f"No flow runs found in states: {states!r}")
            return []
        
        rescheduled_flow_runs = []
        for i, run in enumerate(flow_runs):
            await client.delete_flow_run(flow_run_id=run.id)
            if i < most_recent_n:
                new_run = await client.create_flow_run_from_deployment(
                    deployment_id=run.deployment_id,
                    state=Scheduled(
                        scheduled_time=run.expected_start_time + delay
                    ),
                )
                rescheduled_flow_runs.append(new_run)
            
        return rescheduled_flow_runs


if __name__ == "__main__":
    rescheduled_flow_runs = asyncio.run(
        reschedule_late_flow_runs(
            deployment_name="healthcheck-storage-test",
            delay=timedelta(hours=6),
            most_recent_n=3,
        )
    )
    
    print(f"Rescheduled {len(rescheduled_flow_runs)} flow runs")
        
    assert all(
        run.state.is_scheduled() for run in rescheduled_flow_runs
    )
    assert all(
        run.expected_start_time > datetime.now(timezone.utc)
        for run in rescheduled_flow_runs
    )

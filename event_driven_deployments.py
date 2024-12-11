from prefect import flow, serve
from prefect.events import DeploymentEventTrigger


@flow(log_prints=True)
def upstream_flow():
    print("upstream flow")


@flow(log_prints=True)
def downstream_flow():
    print("downstream flow")


if __name__ == "__main__":
    upstream_deployment = upstream_flow.to_deployment(name="upstream_deployment")
    downstream_deployment = downstream_flow.to_deployment(
        name="downstream_deployment",
        triggers=[
            DeploymentEventTrigger(
                expect={"prefect.flow-run.Completed"},
                match_related={"prefect.resource.name": "upstream_deployment"},
            )
        ],
    )

    serve(upstream_deployment, downstream_deployment)

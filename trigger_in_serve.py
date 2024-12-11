from prefect import flow
from prefect.events import DeploymentCompoundTrigger


@flow(log_prints=True)
def decorated_fn(param_1: str):
    print(param_1)


if __name__=="__main__":
    decorated_fn.deploy(
        name="my-deployment",
        image="my-image-registry/my-image:my-tag",
        triggers=[
            DeploymentCompoundTrigger(
                enabled=True,
                name="my-compound-trigger",
                require="all",
                triggers=[
                    {
                      "type": "event",
                      "match": {"prefect.resource.id": "my.external.resource"},
                      "expect": ["external.resource.pinged"],
                    },
                    {
                      "type": "event",
                      "match": {"prefect.resource.id": "my.external.resource"},
                      "expect": ["external.resource.replied"],
                    },
                ],
                parameters={
                    "param_1": "{{ event }}",
                },
            )
        ],
        work_pool_name="my-work-pool",
    )

from prefect import flow
from prefect.events.schemas.deployment_triggers import DeploymentEventTrigger

order_complete = DeploymentEventTrigger(
    expect={"order.complete"},
    after={"order.created"},
    for_each={"prefect.resource.id"},
    parameters={"user_id": "{{ event.resource.id }}"},
)


@flow(log_prints=True)
def post_order_complete(user_id: str):
    print(f"User {user_id} has completed an order -- doing stuff now")


if __name__ == "__main__":
    post_order_complete.serve(triggers=[order_complete])

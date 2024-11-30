from prefect import flow
from prefect.blocks.core import Block
from prefect.settings import PREFECT_API_URL

def notify_slack(flow, flow_run, state):
    slack_webhook_block = Block.load(
        "slack-webhook/my-slack-webhook"
    )

    slack_webhook_block.notify(
        (
            f"Your job {flow_run.name} entered {state.name} "
            f"with message:\n\n"
            f"See <https://{PREFECT_API_URL.value()}/flow-runs/"
            f"flow-run/{flow_run.id}|the flow run in the UI>\n\n"
            f"Tags: {flow_run.tags}\n\n"
            f"Scheduled start: {flow_run.expected_start_time}"
        )
    )

@flow(on_failure=[notify_slack], retries=1)
def failing_flow():
    raise ValueError("oops!")

if __name__ == "__main__":
    failing_flow()

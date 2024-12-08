from prefect import flow
from prefect.deployments.runner import DockerImage
from prefect.blocks.system import Secret
from myproject.cool import do_something_cool


@flow(log_prints=True)
def my_flow():
    do_something_cool()


if __name__ == "__main__":
    artifact_reg_url: Secret = Secret.load("artifact-reg-url")

    my_flow.deploy(
        name="my-deployment",
        work_pool_name="my-docker-pool",
        image=DockerImage(
            name="my-image",
            tag="test",
            dockerfile="Dockerfile",
            buildargs={"AUTHED_ARTIFACT_REG_URL": artifact_reg_url.get()},
        ),
    )

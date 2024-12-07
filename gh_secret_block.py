from prefect import flow
from prefect.runner.storage import GitRepository
from prefect.blocks.system import Secret


if __name__ == "__main__":

    github_repo = GitRepository(
        url="https://github.com/org/my-private-repo.git",
        credentials={
            "access_token": Secret.load("my-secret-block-with-my-gh-credentials")
        },
    )

    flow.from_source(
        source=github_repo,
        entrypoint="gh_secret_block.py:my_flow",
    ).deploy(
        name="private-github-deploy",
        work_pool_name="my_pool",
    )

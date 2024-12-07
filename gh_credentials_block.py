from prefect import flow
from prefect.runner.storage import GitRepository
from prefect_github import GitHubCredentials


if __name__ == "__main__":

    github_repo = GitRepository(
        url="https://github.com/org/my-private-repo.git",
        credentials=GitHubCredentials.load("my-github-credentials-block"),
    )

    flow.from_source(
        source=github_repo,
        entrypoint="gh_credentials_block.py:my_flow",
    ).deploy(
        name="private-github-deploy",
        work_pool_name="my_pool",
    )

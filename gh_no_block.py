from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/org/my-public-repo.git",
        entrypoint="gh_no_block.py:my_flow",
    ).deploy(
        name="my-github-deployment",
        work_pool_name="my_pool",
    )

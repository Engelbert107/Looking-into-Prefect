if __name__ == "__main__":
    get_repo_info.deploy(
        name="my-deployment-never-pull",
        work_pool_name="my-docker-pool",
        job_variables={"image_pull_policy": "Never"},
        image="my-image:my-tag",
        push=False
    )

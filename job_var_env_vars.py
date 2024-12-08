if __name__ == "__main__":
    get_repo_info.deploy(
        name="my-deployment-never-pull",
        work_pool_name="my-docker-pool",
        job_variables={"env": {"EXTRA_PIP_PACKAGES": "boto3"} },
        image="my-image:my-tag",
        push=False
    )

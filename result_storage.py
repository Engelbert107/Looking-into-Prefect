from prefect import flow, task
from prefect_aws.s3 import S3Bucket # type: ignore

test_block = S3Bucket(bucket_name='test-bucket')
test_block.save('test-block')

# define three tasks
# with different result persistence configuration

@task
def my_task():
    return 42

unpersisted_task = my_task.with_options(persist_result=False)
other_storage_task = my_task.with_options(result_storage=test_block)


@flow(result_storage='s3-bucket/my-dev-block')
def my_flow():

    # this task will use the flow's result storage
    my_task()

    # this task will not persist results at all
    unpersisted_task()

    # this task will persist results to its own bucket using a different S3 block
    other_storage_task()

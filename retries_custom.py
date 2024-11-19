import httpx
from prefect import flow, task


def retry_handler(task, task_run, state) -> bool:
    """Custom retry handler that specifies when to retry a task"""
    try:
        # Attempt to get the result of the task
        state.result()
    except httpx.HTTPStatusError as exc:
        # Retry on any HTTP status code that is not 401 or 404
        do_not_retry_on_these_codes = [401, 404]
        return exc.response.status_code not in do_not_retry_on_these_codes
    except httpx.ConnectError:
        # Do not retry
        return False
    except:
        # For any other exception, retry
        return True


@task(retries=1, retry_condition_fn=retry_handler)
def my_api_call_task(url):
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


@flow
def get_data_flow(url):
    my_api_call_task(url=url)


if __name__ == "__main__":
    get_data_flow(url="https://httpbin.org/status/503")

import httpx
from prefect import flow, task


@task(retries=2, retry_delay_seconds=[1, 10, 100])
def get_data_task(
    url: str = "https://api.brittle-service.com/endpoint"
) -> dict:
    response = httpx.get(url)
    
    # If the response status code is anything but a 2xx, httpx will raise
    # an exception. This task doesn't handle the exception, so Prefect will
    # catch the exception and will consider the task run failed.
    response.raise_for_status()
    
    return response.json()
    

@flow
def get_data_flow():
    get_data_task()


if __name__ == "__main__":
    get_data_flow()

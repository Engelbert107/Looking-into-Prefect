from prefect import flow, task, get_run_logger
import requests
import json


# The data cleaning workflow has visibility into each step, 
# and sends a list of names to the next step of the pipeline.

@task
def fetch(url: str):
    logger = get_run_logger()
    response = requests.get(url)
    raw_data = response.json()
    logger.info(f"Raw response: {raw_data}")
    return raw_data

@task
def clean(raw_data: dict):
    print(raw_data.get('results')[0])
    results = raw_data.get('results')[0]
    logger = get_run_logger()
    logger.info(f"Cleaned results: {results}")
    return results['name']

@flow
def build_names(num: int = 10):
    df = []
    url = "https://randomuser.me/api/"
    logger = get_run_logger()
    copy = num
    while num != 0:
        raw_data = fetch(url)
        df.append(clean(raw_data))
        num -= 1
    logger.info(f"Built {copy} names: {df}")
    return df

if __name__ == "__main__":
    list_of_names = build_names()

import httpx
from datetime import timedelta
from prefect import flow, task
from prefect.tasks import task_input_hash
from typing import Optional


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
def get_url(url: str, params: Optional[dict[str, any]] = None):
    response = httpx.get(url, params=params)
    response.raise_for_status()
    return response.json()


# Now you’re fetching the data you need, but the requests happen sequentially.
# def get_open_issues(repo_name: str, open_issues_count: int, per_page: int = 100):
#     issues = []
#     pages = range(1, -(open_issues_count // -per_page) + 1)
#     for page in pages:
#         issues.append(
#             get_url(
#                 f"https://api.github.com/repos/{repo_name}/issues",
#                 params={"page": page, "per_page": per_page, "state": "open"},
#             )
#         )
#     return [i for p in issues for i in p]


# Tasks expose a submit method that changes the execution from sequential to concurrent.
def get_open_issues(repo_name: str, open_issues_count: int, per_page: int = 100):
    issues = []
    pages = range(1, -(open_issues_count // -per_page) + 1)
    for page in pages:
        issues.append(
            get_url.submit(
                f"https://api.github.com/repos/{repo_name}/issues",
                params={"page": page, "per_page": per_page, "state": "open"},
            )
        )
    return [i for p in issues for i in p.result()]



@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    repo_stats = get_url(f"https://api.github.com/repos/{repo_name}")
    issues = get_open_issues(repo_name, repo_stats["open_issues_count"])
    issues_per_user = len(issues) / len(set([i["user"]["id"] for i in issues]))
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo_stats['stargazers_count']}")
    print(f"Forks 🍴 : {repo_stats['forks_count']}")
    print(f"Average open issues per user 💌 : {issues_per_user:.2f}")


if __name__ == "__main__":
    get_repo_info()


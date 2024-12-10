from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/org/repo.git",
        entrypoint="path/to/my_remote_flow_code_file.py:say_hi",
    ).serve(name="deployment-with-github-storage")

from prefect import flow


@flow(log_prints=True)
def say_hi():
    print("Hello!")

if __name__=="__main__":
    say_hi.serve(name="served and daemonized deployment")

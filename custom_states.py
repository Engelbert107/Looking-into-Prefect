from prefect import flow
from prefect.states import Completed

@flow
def my_flow(work_to_do: bool):
    if not work_to_do:
        return Completed(message="No work to do 💤", name="Skipped")
    else:
        return Completed(message="Work was done 💪")


if __name__ == "__main__":
    my_flow(work_to_do=False)
    print("\nInverse of the previous !\n")
    my_flow(work_to_do=True)

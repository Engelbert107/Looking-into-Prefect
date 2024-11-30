from prefect import task, flow
from prefect.artifacts import create_table_artifact


# def my_fn():
#     highest_churn_possibility = [
#        {'customer_id':'12345', 'name': 'John Smith', 'churn_probability': 0.85 }, 
#        {'customer_id':'56789', 'name': 'Jane Jones', 'churn_probability': 0.65 } 
#     ]

#     create_table_artifact(
#         key="personalized-reachout",
#         table=highest_churn_possibility,
#         description= "# Marvin, please reach out to these customers today!"
#     )


# if __name__ == "__main__":
#     my_fn()

# Define the task
@task
def create_churn_table():
    highest_churn_possibility = [
        {'customer_id': '12345', 'name': 'John Smith', 'churn_probability': 0.85},
        {'customer_id': '56789', 'name': 'Jane Jones', 'churn_probability': 0.65}
    ]
    
    # Create the table artifact inside the task
    create_table_artifact(
        key="personalized-reachout",
        table=highest_churn_possibility,
        description="# Marvin, please reach out to these customers today!"
    )

# Define the flow
@flow
def my_fn():
    create_churn_table()

# Run the flow
if __name__ == "__main__":
    my_fn()

from prefect import flow, task
from prefect.artifacts import (
    create_image_artifact,
)


@task
def create_image():
    # Do something to create an image and upload to a url
    image_url = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmQydzBjOHQ2M3BhdWJ4M3V1MGtoZGxuNmloeGh6b2dvaHhpaHg0eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3KC2jD2QcBOSc/giphy.gif"
    create_image_artifact(image_url=image_url, description="A gif.", key="gif")
    return image_url


@flow
def my_flow():
    return create_image()


if __name__ == "__main__":
    image_url = my_flow()
    print(f"Image URL: {image_url}")

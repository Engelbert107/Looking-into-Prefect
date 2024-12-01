import asyncio
from prefect.concurrency.sync import concurrency


async def process_data(data):
    print(f"Processing: {data}")
    await asyncio.sleep(1)
    return f"Processed: {data}"


async def main():
    data_items = list(range(100))
    processed_data = []

    while data_items:
        with concurrency("data-processing", occupy=5):
            chunk = [data_items.pop() for _ in range(5)]
            processed_data += await asyncio.gather(
                *[process_data(item) for item in chunk]
            )

    print(processed_data)


if __name__ == "__main__":
    asyncio.run(main())

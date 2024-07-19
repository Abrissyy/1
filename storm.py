import sys
import asyncio
import aiohttp
import time

async def send_requests(url, port, duration):
    start_time = time.time()
    num_requests = 0

    async with aiohttp.ClientSession() as session:
        while time.time() - start_time < duration:
            try:
                async with session.get(f"{url}:{port}") as response:
                    if response.status == 200:
                        num_requests += 1
            except aiohttp.ClientError as e:
                print(f"Request error: {e}")

    print(f"Total requests sent: {num_requests}")

async def main():
    if len(sys.argv) != 4:
        print("Usage: python storm.py <url> <duration> <port>")
        return

    url = sys.argv[1]
    duration = int(sys.argv[2])
    port = sys.argv[3]

    print(f"Sending requests to http://{url}:{port} for {duration} seconds...")

    tasks = []
    for _ in range(1000):  # Można dostosować ilość równoczesnych żądań
        task = asyncio.create_task(send_requests(url, port, duration))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print(f"All requests finished to http://{url}:{port}")

if __name__ == "__main__":
    asyncio.run(main())

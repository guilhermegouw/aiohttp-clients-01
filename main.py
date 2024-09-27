import asyncio

from aiohttp import ClientError, ClientSession


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Error: {response.status}")
    except ClientError as e:
        print(f"Error: fetching URL: {e}")


async def main():
    async with ClientSession() as session:
        tasks = []
        urls = ["http://httpbin.org/get", "http://httpbin.org/delay/1"]

        for url in urls:
            tasks.append(asyncio.create_task(fetch(session, url)))

        results = await asyncio.gather(*tasks)
        print(results)


asyncio.run(main())

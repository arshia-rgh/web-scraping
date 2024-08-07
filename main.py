import aiohttp
import asyncio


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception("Fail to load the page")

            return await response.text()


url = "https://bama.ir/car"

print(asyncio.run(fetch_data(url)))

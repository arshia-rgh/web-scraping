import aiohttp
import asyncio
from url import base_url


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            return content

print(asyncio.run(fetch(base_url.build())))

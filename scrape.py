from urls.url import generate_urls
import aiohttp
from bs4 import BeautifulSoup
from collections import defaultdict
import asyncio


class Scrape:
    urls = generate_urls()
    html_content = defaultdict(list)

    @classmethod
    async def fetch_html_content(cls):
        async with aiohttp.ClientSession() as session:
            tasks = [session.get(url) for url in cls.urls]
            response = await asyncio.gather(*tasks)
            return response

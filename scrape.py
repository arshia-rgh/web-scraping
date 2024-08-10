from urls.url import generate_urls
import aiohttp
from bs4 import BeautifulSoup
from collections import defaultdict
import asyncio


class Scrape:
    def __init__(self):
        self.urls = generate_urls()
        self.html_content = defaultdict(list)

    async def fetch_html_content(self):
        async with aiohttp.ClientSession() as session:
            tasks = [session.get(url) for url in self.urls]
            responses = await asyncio.gather(*tasks)
            return responses


scrape = Scrape()
print(asyncio.run(scrape.fetch_html_content()))

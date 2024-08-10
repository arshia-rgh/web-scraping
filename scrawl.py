import asyncio
from collections import defaultdict

import aiohttp

from urls.url import generate_urls


class Scrawl:
    def __init__(self):
        self.urls = generate_urls()
        self._html_content = None
        self._html_content_fetched = False

    async def fetch_url_content(self, session, url):
        async with session.get(url) as response:
            text = await response.text()
            self._html_content[url].append(text)
            return text

    async def fetch_all_html_content(self):
        self._html_content = defaultdict(list)

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_url_content(session, url) for url in self.urls]
            await asyncio.gather(*tasks)
        self._html_content_fetched = True

    def __getattr__(self, name):
        if name == "html_content" and not self._html_content_fetched:
            asyncio.run(self.fetch_all_html_content())
            return self._html_content
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute {name}")


scrawl = Scrawl()

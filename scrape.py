from bs4 import BeautifulSoup
from scrawl import scrawl_instance


class Scrape:
    def __init__(self):
        self.soup = {}
        self.htm_content = scrawl_instance.html_content
        self.parse_html_content()

    def parse_html_content(self):
        for url, content_list in self.htm_content.items():
            self.soup[url] = [BeautifulSoup(content, "html.parser") for content in content_list]


scrape = Scrape()
print(scrape.soup)

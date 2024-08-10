from urllib.parse import urljoin
from .validator_category import validate_category
from .url_setting import *


class Url:
    def __init__(self, base_url):
        self.base_url = base_url
        self.category = ""
        self.brand = ""

    @validate_category
    def set_category(self, category):
        self.category = category

        return self

    def set_brand(self, brand):
        self.brand = brand

        return self

    def build(self):
        path = f"{self.category}/{self.brand}"

        return urljoin(self.base_url, path)

    @classmethod
    def add_url(cls, base_url, category="", brand=""):
        url_instance = cls(base_url=base_url)
        url_instance.set_category(category=category)
        url_instance.set_brand(brand=brand)
        return url_instance.build()


def generate_urls():
    urls = []

    for category in categories_list:
        if brands_list:
            for brand in brands_list:
                url = Url.add_url(base_url=base_url, category=category, brand=brand)
        else:
            url = Url.add_url(base_url=base_url, category=category)

        urls.append(url)

    return urls

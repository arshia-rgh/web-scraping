from urllib.parse import urljoin
from validator_category import validate_category


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


url = Url("https://bama.ir/")
final_url = url.set_category("car").set_brand("audi").build()
print(final_url)

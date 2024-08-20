import pytest

from scrap import Scrape
from scrawl import Scrawl
from urls.url import Url


#  <--- test_urls --->
@pytest.fixture
def url_instance():
    return Url("www.test.com")


@pytest.fixture
def generate_urls_setup(monkeypatch):
    monkeypatch.setattr("urls.url.categories_list", ["car", "truck"])
    monkeypatch.setattr("urls.url.brands_list", ["toyota", "ford"])
    monkeypatch.setattr('urls.url.base_url', 'www.test.com')


#  <--- test_scrawl --->
@pytest.fixture
def scrawl_instance():
    return Scrawl()


#  <--- test_scrap --->
@pytest.fixture
def scrape_instance():
    return Scrape()

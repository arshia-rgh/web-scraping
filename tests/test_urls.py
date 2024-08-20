import pytest

from tests.conftest import url_instance
from urls.url import Url, generate_urls


class TestUrl:

    def test_initiate_Url(self, url_instance):
        assert isinstance(url_instance, Url)
        assert url_instance.category == ""
        assert url_instance.base_url == "www.test.com"
        assert url_instance.brand == ""

    def test_set_category(self, url_instance):
        url_instance.set_category("car")
        assert url_instance.category == "car"

        with pytest.raises(ValueError):
            url_instance.set_category("wrong category")

    def test_set_brand(self, url_instance):
        url_instance.set_brand("toyota")
        assert url_instance.brand == "toyota"

    def test_build(self, url_instance):
        assert url_instance.build() == "www.test.com"
        url_instance.set_category("truck")
        url_instance.set_brand("toyota")
        assert url_instance.build() == "www.test.com/truck/toyota"

    def test_add_url(self):
        assert Url.add_url(
            base_url="www.test.com",
            category="car",
            brand="toyota"

        ) == "www.test.com/car/toyota"


class TestGenerateUrls:

    def test_generate_urls_with_brands(self, generate_urls_setup):
        expected_urls = [
            "www.test.com/car/ford",
            "www.test.com/car/toyota",
            "www.test.com/truck/ford",
            "www.test.com/truck/toyota",
        ]
        assert set(generate_urls()) == set(expected_urls)

    def test_generate_urls_without_brands(self, generate_urls_setup, monkeypatch):
        monkeypatch.setattr("urls.url.brands_list", [])
        expected_urls = [
            "www.test.com/car",
            "www.test.com/truck",
        ]
        assert set(generate_urls()) == set(expected_urls)

    def test_generate_urls_without_categories(self, generate_urls_setup, monkeypatch):
        monkeypatch.setattr('urls.url.categories_list', [])

        assert generate_urls() == ["www.test.com"]

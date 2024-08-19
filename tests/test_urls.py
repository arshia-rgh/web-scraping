import pytest
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

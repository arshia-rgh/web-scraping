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

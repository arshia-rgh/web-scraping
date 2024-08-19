import pytest
from urls.url import Url, generate_urls


class TestUrl:

    def test_initiate_Url(self):
        url = Url("www.test.com")
        assert isinstance(url, Url)
        assert url.category == ""
        assert url.base_url == "www.test.com"
        assert url.brand == ""

    def test_set_category(self):
        url = Url("www.test.com")
        url.set_category("car")
        assert url.category == "car"

        with pytest.raises(ValueError):
            url.set_category("wrong")

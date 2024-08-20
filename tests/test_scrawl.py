import pytest

from scrawl import Scrawl


class TestScrawl:
    def test_scrawl_initiate(self, generate_urls_setup):
        expected_urls = [
            "www.test.com/car/ford",
            "www.test.com/car/toyota",
            "www.test.com/truck/ford",
            "www.test.com/truck/toyota",
        ]
        scrawl = Scrawl()
        assert isinstance(scrawl, Scrawl)
        assert set(scrawl.urls) == set(expected_urls)

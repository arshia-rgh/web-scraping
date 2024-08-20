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
        assert scrawl._html_content is None
        assert scrawl._html_content_fetched is False
        assert set(scrawl.urls) == set(expected_urls)

    @pytest.mark.asyncio
    async def test_fetch_all_html_content(self):
        scrawl = Scrawl()

        await scrawl.fetch_all_html_content()
        assert scrawl._html_content_fetched is True
        assert isinstance(scrawl._html_content, dict)

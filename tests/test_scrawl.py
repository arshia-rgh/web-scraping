import pytest

from scrawl import Scrawl


class TestScrawl:

    def test_scrawl_initiate(self, generate_urls_setup, scrawl_instance):
        expected_urls = [
            "www.test.com/car/ford",
            "www.test.com/car/toyota",
            "www.test.com/truck/ford",
            "www.test.com/truck/toyota",
        ]
        assert isinstance(scrawl_instance, Scrawl)
        assert scrawl_instance._html_content is None
        assert scrawl_instance._html_content_fetched is False
        assert set(scrawl_instance.urls) == set(expected_urls)

    @pytest.mark.asyncio
    async def test_fetch_all_html_content(self, scrawl_instance):
        await scrawl_instance.fetch_all_html_content()
        assert scrawl_instance._html_content_fetched is True
        assert isinstance(scrawl_instance._html_content, dict)

    @pytest.mark.asyncio
    async def test_getter(self, scrawl_instance):
        assert scrawl_instance._html_content_fetched is False
        assert scrawl_instance._html_content is None
        html_content = await scrawl_instance.html_content

        assert scrawl_instance._html_content_fetched is True
        assert isinstance(html_content, dict)

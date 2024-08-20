from unittest.mock import patch, MagicMock

import pytest

from scrap import Scrape


class TestScrape:

    @patch('scrap.scrawl_instance')
    def test_initialization(self, mock_scrawl_instance):
        mock_scrawl_instance.html_content = {}
        scrape = Scrape()
        assert isinstance(scrape, Scrape)
        assert scrape.soup == {}
        assert scrape.htm_content == {}

    @patch("scrap.scrawl_instance")
    def test_parse_html_content(self, mock_scrawl_instance):
        mock_scrawl_instance.html_content = {
            "https://example.com": [
                "<html><head><title>Example</title></head><body></body></html>"
            ]

        }
        scrape = Scrape()
        assert "https://example.com" in scrape.soup
        assert len(scrape.soup["https://example.com"]) == 1
        assert scrape.soup["https://example.com"][0].title.string == "Example"


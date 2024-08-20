from unittest.mock import patch

import pytest

from scrap import Scrape


class TestScrape:

    @patch('scrap.scrawl_instance')
    def test_initialization(self, mock_scrawl_instance, scrape_instance):
        mock_scrawl_instance.html_content = {}
        assert isinstance(scrape_instance, Scrape)
        assert scrape_instance.soup == {}
        assert scrape_instance.htm_content == {}

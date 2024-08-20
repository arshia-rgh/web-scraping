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

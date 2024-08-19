import pytest
from urls.url import Url


@pytest.fixture
def url_instance():
    return Url("www.test.com")

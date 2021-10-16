"""This is a main testing module of the project."""

import os

from page_loader.download import download
from page_loader.naming import get_name

TEST_URL = 'https://ru.hexlet.io/courses'


def test_get_name():
    """Test for checking naming parsing of web page URL."""
    assert get_name(
        'https://ru.hexlet.io/courses',
    ) == 'ru-hexlet-io-courses.html'


def test_download(requests_mock, tmp_path):
    """Test for download function: check file existing and its content.

    Args:
        requests_mock: mock for HTTP request.
        tmp_path: temporary path for testing.
    """
    requests_mock.get(TEST_URL, text='data')
    download(TEST_URL, tmp_path)
    with open(os.path.join(tmp_path, get_name(TEST_URL))) as test_file:
        test_content = test_file.read()
        assert test_content == 'data'

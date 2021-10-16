"""This is a main testing module of the project."""

import os
from page_loader.download import download
from page_loader.naming import get_name


def test_get_name():
    """Test for checking naming parsing of web page URL."""
    assert get_name(
        'https://ru.hexlet.io/courses',
    ) == 'ru-hexlet-io-courses.html'


def test_download(requests_mock, tmp_path):
    requests_mock.get('https://ru.hexlet.io/courses', text='data')
    download('https://ru.hexlet.io/courses', tmp_path)
    with open(os.path.join(tmp_path, get_name('https://ru.hexlet.io/courses'))) as file:
        content = file.read()
        assert content == 'data'

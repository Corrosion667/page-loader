"""This is a main testing module of the project."""

import os

from page_loader.download import download
from page_loader.naming import 
TEST_URL = 'https://ru.hexlet.io/courses'


def test_download(requests_mock, tmp_path):  # noqa: WPS218, WPS210
    """Test download function: check file existing, its content and local resources.

    Args:
        requests_mock: mock for HTTP request.
        tmp_path: temporary path for testing.
    """
    with open('tests/fixtures/test_page.html') as web_page:
        html_before = web_page.read()
    with open('tests/fixtures/result_page.html') as result_page:
        html_after = result_page.read()

    requests_mock.get(TEST_URL, text=html_before)
    requests_mock.get('https://ru.hexlet.io/assets/professions/nodejs.png')
    requests_mock.get('https://ru.hexlet.io/assets/application.css')
    requests_mock.get('https://ru.hexlet.io/packs/js/runtime.js')

    download_path = download(TEST_URL, tmp_path)
    image_path = os.path.join(
        tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png',
    )
    css_path = os.path.join(
        tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-assets-application.css',
    )
    js_path = os.path.join(
        tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-packs-js-runtime.js',
    )
    html_path = os.path.join(
        tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-courses.html',
    )

    assert os.path.exists(download_path)
    assert os.path.exists(image_path)
    assert os.path.exists(css_path)
    assert os.path.exists(js_path)
    assert os.path.exists(html_path)

    with open(os.path.join(tmp_path, download_path)) as test_file:
        test_content = test_file.read()
        assert test_content == html_after

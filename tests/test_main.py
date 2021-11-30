"""This is a main testing module of the project."""

import os

from page_loader.download import download

TEST_URL = 'https://ru.hexlet.io/courses'

LOCALS_FIXTURES = (
    'tests/fixtures/page.html',
    'tests/fixtures/image.png',
    'tests/fixtures/script.js',
    'tests/fixtures/style.css',
)

MOCKING_LINKS = (
    TEST_URL,
    'https://ru.hexlet.io/assets/professions/nodejs.png',
    'https://ru.hexlet.io/packs/js/runtime.js',
    'https://ru.hexlet.io/assets/application.css',
)


def test_download(requests_mock, tmp_path):
    """Test download function: check downloaded html file, its content and local resources.

    Args:
        requests_mock: mock for HTTP request.
        tmp_path: temporary path for testing.
    """
    for fixture, link in zip(LOCALS_FIXTURES, MOCKING_LINKS):
        with open(fixture, 'rb') as fixture_file:
            mocking_content = fixture_file.read()
        requests_mock.get(link, content=mocking_content)

    download_path = download(TEST_URL, tmp_path)

    downloaded_locals = (
        os.path.join(
            tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-courses.html',
        ),
        os.path.join(
            tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png',
        ),
        os.path.join(
            tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-packs-js-runtime.js',
        ),
        os.path.join(
            tmp_path, 'ru-hexlet-io-courses_files/ru-hexlet-io-assets-application.css',
        ),
    )
    for fixture, local in zip(LOCALS_FIXTURES, downloaded_locals):  # noqa: WPS440
        with open(fixture, 'rb') as fixture_file:  # noqa: WPS440
            with open(local, 'rb') as downloaded_file:
                assert fixture_file.read() == downloaded_file.read()

    with open(download_path) as downloaded_html:
        with open('tests/fixtures/result.html') as result_fixture:
            assert downloaded_html.read() == result_fixture.read()

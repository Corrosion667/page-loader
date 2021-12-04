"""This is a module to test programm for error raising."""

import os

import pytest
import requests
from page_loader.download import ExpectedError, download

UNACCESSABLE_RIGHTS = 000
ACCESSABLE_RIGHTS = 777
NETWORK_ERROR_CODE = 404
TEST_URL = 'https://ru.hexlet.io/courses'


def test_download_wrong_path(tmp_path):
    """Do not allow to pass to script non-existent paths.

    Args:
        tmp_path: temporary path for testing.
    """
    wrong_path = os.path.join(tmp_path, '/wrong_folder')
    with pytest.raises(ExpectedError):
        download(TEST_URL, wrong_path)


def test_unaccessable(tmp_path):
    """Do not allow to pass to programm unaccessable folders.

    Args:
        tmp_path: temporary path for testing.
    """
    unaccessable_path = os.path.join(tmp_path, 'wrong_folder')
    os.mkdir(unaccessable_path)
    with pytest.raises(ExpectedError):
        os.chmod(unaccessable_path, UNACCESSABLE_RIGHTS)
        download(TEST_URL, unaccessable_path)
    os.chmod(unaccessable_path, ACCESSABLE_RIGHTS)


def test_html_download_error(requests_mock, tmp_path):
    """Test whether programm raises exception if network error took place.

    Error happens during download of main web page.

    Args:
        requests_mock: mock for HTTP request.
        tmp_path: temporary path for testing.
    """
    requests_mock.get(TEST_URL, status_code=NETWORK_ERROR_CODE)
    with pytest.raises(requests.exceptions.RequestException):
        download(TEST_URL, tmp_path)


def test_local_download_error(requests_mock, tmp_path):
    """Test whether programm raises exception if network error took place.

    Error happens during download of local resource.

    Args:
        requests_mock: mock for HTTP request.
        tmp_path: temporary path for testing.
    """
    with open('tests/fixtures/page.html', 'rb') as fixture_file:
        mocking_content = fixture_file.read()
    requests_mock.get(TEST_URL, content=mocking_content)
    requests_mock.get(
        'https://ru.hexlet.io/assets/professions/nodejs.png',
        status_code=NETWORK_ERROR_CODE,
    )
    with pytest.raises(requests.exceptions.RequestException):
        download(TEST_URL, tmp_path)

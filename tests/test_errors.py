"""This is a module to test programm for error raising."""

import os

import pytest
from page_loader.download import download

UNACCESSABLE_RIGHTS = 000
TEST_URL = 'https://ru.hexlet.io/courses'


def test_download_wrong_path(tmp_path):
    """Do not allow to pass to script non-existent paths.

    Args:
        tmp_path: temporary path for testing.
    """
    wrong_path = os.path.join(tmp_path, '/wrong_folder')
    with pytest.raises(FileNotFoundError):
        download(TEST_URL, wrong_path)


def test_unaccessable(tmp_path):
    """Do not allow to pass to programm unaccessable folders.

    Args:
        tmp_path: temporary path for testing.
    """
    unaccessable_path = os.path.join(tmp_path, 'wrong_folder')
    os.mkdir(unaccessable_path)
    os.chmod(unaccessable_path, UNACCESSABLE_RIGHTS)
    with pytest.raises(PermissionError):
        download(TEST_URL, unaccessable_path)

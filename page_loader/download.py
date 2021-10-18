"""Module to download web pages via their URLs."""

import os

import requests
from page_loader.naming import get_name

DEFAULT_PATH = '/app'


def download(url, directory=DEFAULT_PATH):
    """Docstring.

    Args:
        url: url.
        directory: directory.

    Returns:
        Full path of download including file name.
    """
    response = requests.get(url)
    file_name = '{0}.html'.format(get_name(url))
    if directory == DEFAULT_PATH:
        download_path = os.path.join(os.getcwd(), file_name)
    else:
        download_path = os.path.join(directory, file_name)
    with open(download_path, 'w') as new_file:
        new_file.write(response.text)
    return download_path

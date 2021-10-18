"""Module to download web pages via their URLs."""

import os

import requests
from page_loader.naming import get_name

default_path = os.getcwd()


def download(url, directory=default_path):
    """Docstring.

    Args:
        url: url.
        directory: directory.

    Returns:
        Full path of download including file name.
    """
    response = requests.get(url)
    file_name = '{0}.html'.format(get_name(url))
    download_path = os.path.join(directory, file_name)
    with open(download_path, 'w') as new_file:
        new_file.write(response.text)
    return download_path

"""Module to download web pages via their URLs."""

import os

import requests
from page_loader.naming import get_name


def download(url, directory):
    """Docstring.

    Args:
        url: url.
        directory: directory.
    """
    response = requests.get(url)
    file_name = get_name(url)
    with open(os.path.join(directory, file_name), 'w') as new_file:
        new_file.write(response.text)

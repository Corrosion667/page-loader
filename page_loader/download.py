"""Module to download web pages via their URLs."""

import os

import requests
from page_loader.naming import html_name

default_path = os.getcwd()


def download(url, directory=default_path):
    """Download web page to the selected directory.

    Args:
        url: url of the web page.
        directory: directory where to download the page.

    Returns:
        Full path of download including file name.
    """
    response = requests.get(url)
    file_name = html_name(url)
    download_path = os.path.join(directory, file_name)
    with open(download_path, 'w') as new_file:
        new_file.write(response.text)
    return download_path

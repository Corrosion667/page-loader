"""Module to download web pages via their URLs."""

import os
from urllib.parse import urlparse

import requests
from page_loader.locals import get_and_replace_locals
from page_loader.naming import folder_name, html_name

default_path = os.getcwd()


def download(url, directory=default_path):
    """Download web page and locals to the selected directory.

    Args:
        url: url of the web page.
        directory: directory where to download the page.

    Returns:
        Full path of download including file name.
    """
    os.mkdir(os.path.join(directory, folder_name(url)))
    response = requests.get(url)
    file_name = html_name(url)
    download_path = os.path.join(directory, file_name)
    with open(download_path, 'w') as new_file:
        new_file.write(response.text)
    downloads = get_and_replace_locals(download_path, url)
    download_locals(downloads, url)
    return download_path


def download_locals(downloads, url):  # noqa: WPS210
    """Download local resources.

    Args:
        downloads: list of links and file paths for downloads.
        url: url of the web page.
    """
    for each in downloads:
        link, path = each
        if not urlparse(link).netloc:
            link = '{0}{1}'.format(urlparse(url).netloc, link)
        response = requests.get(link, stream=True)
        with open(path, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=None):
                local_file.write(chunk)

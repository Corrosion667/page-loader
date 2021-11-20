"""Module for getting names depending on the URL of the page."""

import pathlib
import re
from urllib.parse import urlparse


def get_name(url):
    """Get basic name for downloads depending on the URL of page.

    Args:
        url: URL of the web page.

    Returns:
        Generated name.
    """
    prefix = urlparse(url).scheme
    body = re.sub(r'^{0}://'.format(prefix), '', url)
    return re.sub(r'[^a-zA-Z0-9]', '-', body)


def html_name(url):
    """Get name for downloaded html file depending on the URL of page.

    Args:
        url: URL of the web page.

    Returns:
        Generated name for html file.
    """
    return '{0}.html'.format(get_name(url))


def folder_name(url):
    """Get name for folder to download resources depending on the URL of page.

    Args:
        url: URL of the web page.

    Returns:
        Generated name for downloads directory.
    """
    return '{0}_files'.format(get_name(url))


def locals_name(url, link):
    """Get name for local file depending on URL of page and link of the file.

    Args:
        url: URL of the web page.
        link: src or href for the resource.

    Returns:
        Generated name for image file.
    """
    prefix = re.sub(r'[^a-zA-Z0-9]', '-', urlparse(url).netloc)
    file_name = '{}{}'
    return '{0}_files'.format(get_name(url))

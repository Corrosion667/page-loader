"""Module for getting names depending on the URL of the page."""

import re
from urllib.parse import urlparse


def get_name(url):
    """Get name for downloads depending on the URL of page.

    Args:
        url: URL of the web page.

    Returns:
        Generated name for files.
    """
    prefix = urlparse(url).scheme
    body = re.sub(r'^{0}...'.format(prefix), '', url)
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

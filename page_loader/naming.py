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
    return '{0}.html'.format(get_name(url)[:-1])


def folder_name(url):
    """Get name for folder to download resources depending on the URL of page.

    Args:
        url: URL of the web page.

    Returns:
        Generated name for downloads directory.
    """
    return '{0}_files'.format(get_name(url)[:-1])


def locals_name(url, link):
    """Get name for local file depending on URL of page and link of the file.

    Args:
        url: URL of the web page.
        link: src or href for the resource.

    Returns:
        Generated name for image file.
    """
    if not urlparse(link).netloc:
        link = '{0}{1}'.format(urlparse(url).netloc, link)
    file_ext = pathlib.Path(link).suffix
    if not file_ext:
        file_ext = '.html'
    body = re.sub(r'{0}$'.format(file_ext), '', link)
    return '{0}{1}'.format(get_name(body), file_ext)

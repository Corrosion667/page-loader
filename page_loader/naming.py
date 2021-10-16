"""Module for getting names depending on the URL of the page."""

import re
from urllib.parse import urlparse


def get_name(url):
    """Get name for dounloads depending on the URL of page.

    Args:
        url: ULR of the web page.

    Returns:
        Generated name for files.
    """
    prefix = urlparse(url).scheme
    name = re.sub(r'^{0}...'.format(prefix), '', url)
    return '{0}.html'.format(
        re.sub(r'[^a-zA-Z0-9]', '-', name),
    )

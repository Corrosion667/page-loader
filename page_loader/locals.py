"""Module for working with local resources."""

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from page_loader.naming import locals_name

LOCALS = ['img', 'link', 'script']


def is_local(src, url):
    """Criteria wether to download selected object or not.

    Args:
        src: link to the resource.
        url: url of the web page where resource is used.

    Returns:
        Boolean of affiliation of the objects's src to local ones.
    """
    domain = urlparse(url).netloc
    return urlparse(src).netloc in {domain, ''}


def get_locals(url):
    """Get list of tuples: local resources and file names for them to be downloaded.

    Args:
        url: url of the web page to be parsed.

    Returns:
        List of locally stored resources and names for files to download.
    """
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    urls = []
    for each in LOCALS:
        for link in soup.find_all(each):
            if each != 'link':
                try:
                    if is_local(link['src'], url):
                        urls.append(
                            (link['src'], locals_name(url, link['src'])))
                except KeyError:
                    continue
            try:
                if is_local(link['href'], url):
                    urls.append((link['href'], locals_name(url, link['href'])))
            except KeyError:
                continue
    return urls

"""Module for working with local resources."""

import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from page_loader.naming import folder_name

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


def get_local_links(url):
    """Get list of tuples: local resources and file names for them to be downloaded.

    Args:
        url: url of the web page to be parsed.

    Returns:
        List of locally stored resources and names for dowload files.
    """
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tags = []
    for each in LOCALS:
        tags.extend(soup.find_all(each))
    urls = []
    for link in tags:
        try:
            if is_local(link['src'], url):
                urls.append(link['src'])
        except KeyError:
            if is_local(link['href'], url):
                urls.append(link['href'])
                continue
    return urls


def download_locals(url, directory):
    os.mkdir(os.path.join(directory, folder_name(url)))
    links = get_images_links(url)
    for link in links:
        pass

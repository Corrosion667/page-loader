"""Module for working with web images."""

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def is_local(src, url):
    """Criteria wether to download selected iamge or not.

    Args:
        src: link to the image.
        url: url of the web page where image is used.

    Returns:
        Boolean of affiliation of the image's src to local ones.
    """
    domain = urlparse(url).netloc
    return urlparse(src).netloc in {domain, ''}


def get_images_links(url):
    """Get list of local images to be downloaded.

    Args:
        url: url of the web page to be parsed.

    Returns:
        List of locally stored images.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return [img['src'] for img in img_tags if is_local(img['src'], url)]

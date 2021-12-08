"""Module for working with local resources."""

from typing import List
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from page_loader.naming import locals_path

# FIXME: нейминг, что за locals?
LOCALS = ('img', 'link', 'script')

# FIXME: нейминг, конснтанты именуем в UPPERCASE
source = 'src'
hyperlink = 'href'


def is_local(src: str, url: str) -> bool:
    """Criteria wether to download selected object or not.

    Args:
        src: link to the resource.
        url: url of the web page where resource is used.

    Returns:
        Boolean of affiliation of the objects's src to local ones.
    """
    domain = urlparse(url).netloc
    return urlparse(src).netloc in {domain, ''}


def get_and_replace_locals(path_to_html: str, url: str) -> List[tuple]:  # noqa: C901, WPS231, E501
    """Replace links in downloaded html page from web links to local files.

    Get list of tuples: links with local resources and file paths for downloads.

    Args:
        path_to_html: dowloaded html file.
        url: url of the web page.

    Returns:
        Links for downloads and local paths for them.
    """
    with open(path_to_html) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    urls = []
    for tag in LOCALS:
        # FIXME: findALl может сразу несколько тегов искать, может чуть код упростить
        for link in soup.findAll(tag):
            try:
                # FIXME: если добавится еще один вид тегов со своими атрибутами, то сильно разрастется if этот
                ref = link[hyperlink] if tag == 'link' else link[source]
            except KeyError:
                continue
            if not is_local(ref, url):
                continue
            path = locals_path(ref, url)
            urls.append((ref, path))

            # FIXME: та же самая сложность с if, сейчас это работает, но если вдруг появится третий тег с другим атрибутом, то придется сильно переписывать уже
            if tag != 'link':
                link[source] = path
                continue
            link[hyperlink] = path
    with open(path_to_html, 'w') as new_html:
        new_html.write(soup.prettify())
    return urls

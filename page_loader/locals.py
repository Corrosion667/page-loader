"""Module for working with local resources."""

from typing import List
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from page_loader.naming import locals_path

IMG, LINK, SCRIPT, SOURCE, HYPERLINK = 'img', 'link', 'script', 'src', 'href'
resource_tags_map = {
    IMG: SOURCE,
    LINK: HYPERLINK,
    SCRIPT: SOURCE,
}


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


def prepare_link(link: str, url: str) -> str:
    """Check if link has scheme and netloc and add them if missing.

    Args:
        link: initial link for download resource.
        url: url of the web page where resource is used.

    Returns:
        Link with scheme and netloc.
    """
    if not urlparse(link).netloc:
        link = '{0}://{1}{2}'.format(
            urlparse(url).scheme,
            urlparse(url).netloc,
            link,
        )
    return link


def get_and_replace_links(path_to_html: str, url: str) -> List[tuple]:  # noqa: WPS231, E501
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
    for tag in resource_tags_map.keys():
        # FIXME: findALl может сразу несколько тегов искать, может чуть код упростить
        for link in soup.findAll(tag):
            try:
                ref = link[resource_tags_map[tag]]
            except KeyError:
                continue
            if not is_local(ref, url):
                continue
            path = locals_path(ref, url)
            urls.append((prepare_link(ref, url), path))
            link[resource_tags_map[tag]] = path
    with open(path_to_html, 'w') as new_html:
        new_html.write(soup.prettify())
    return urls

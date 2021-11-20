"""Module for working with local resources."""  # noqa: WPS232

from urllib.parse import urlparse

from bs4 import BeautifulSoup
from page_loader.naming import locals_path

LOCALS = ('img', 'link', 'script')
source = 'src'
hyperlink = 'href'


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


def get_and_replace_locals(path_to_html, url):  # noqa: C901, WPS210, WPS231
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
    for each in LOCALS:  # noqa: WPS327
        for link in soup.findAll(each):  # noqa: WPS327
            if each != 'link':
                try:
                    if is_local(link[source], url):
                        path = locals_path(link[source], url)  # noqa: WPS220
                        urls.append((link[source], path))  # noqa: WPS220
                        link[source] = path  # noqa: WPS220
                except KeyError:
                    continue
            try:
                if is_local(link[hyperlink], url):
                    path = locals_path(link[hyperlink], url)
                    urls.append((link[hyperlink], path))
                    link[hyperlink] = path
            except KeyError:
                continue
    with open(path_to_html, 'w') as new_html:
        new_html.write(soup.prettify())
    return urls

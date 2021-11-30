"""Module to download web pages via their URLs."""

import os
from typing import List
from urllib.parse import urlparse

import requests
from colorama import Fore
from page_loader.locals import get_and_replace_locals
from page_loader.naming import folder_name, html_name
from progress.spinner import Spinner


class DownloadSpinner(Spinner):
    """Custom spinner to show progress of local downloads."""

    phases = [Fore.GREEN + '✓ ' + Fore.RESET]  # noqa: WPS336


default_path = os.getcwd()


def download(url: str, directory: str = default_path) -> str:
    """Download web page and locals to the selected directory.

    Args:
        url: url of the web page.
        directory: directory where to download the page.

    Returns:
        Full path of download including html file name.

    Raises:
        FileNotFoundError: user have chosen incorrect output directory.
        PermissionError: user do not have access to the selected folder.
        OSError: unexpected error.
    """
    try:
        os.mkdir(os.path.join(directory, folder_name(url)))
    except FileNotFoundError:
        raise FileNotFoundError(
            'Make sure you have choosen a vaild directory path: {0}'.format(
                directory,
            ),
        )
    except PermissionError:
        raise PermissionError(
            'You do not have access to directory: {0}'.format(
                directory,
            ),
        )
    except OSError:
        raise OSError('Unknown error happened')
    download_path = download_html(url, directory)
    downloads = get_and_replace_locals(download_path, url)
    download_locals(downloads, url, directory)
    return download_path


def download_html(url: str, directory: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        raise requests.exceptions.RequestException(
            'Network error. Statis code is {0}'.format(
                requests.get(url).status_code,
            ),
        )
    file_name = html_name(url)
    download_path = os.path.join(directory, file_name)
    with open(download_path, 'wb') as new_file:
        new_file.write(response.content)
    return download_path


def download_locals(downloads: List[tuple], url: str, directory: str) -> None:  # noqa: WPS210, E501
    """Download local resources.

    Args:
        downloads: pairs of links and paths for downloads.
        url: url of the web page.
        directory: folder set by user where scripts downloads everything.
    """
    spinner = DownloadSpinner()
    for pair in downloads:
        link, path = pair
        if not urlparse(link).netloc:
            link = '{0}://{1}{2}'.format(
                urlparse(url).scheme,
                urlparse(url).netloc,
                link,
            )
        response = requests.get(link, stream=True)
        path = os.path.join(directory, path)
        with open(path, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=None):
                local_file.write(chunk)
        spinner.next()
        print(link)  # noqa: WPS421

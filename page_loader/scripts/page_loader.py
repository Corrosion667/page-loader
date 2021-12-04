#!/usr/bin/env python3
"""This program downloads a page from the network."""
import argparse
import logging

import requests
from page_loader.download import ExpectedError, default_path, download
from page_loader.logging_settings import LOGGING_CONFIG

SUCCESS = "Page was successfully downloaded into '{0}'"

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('default_logger')


def main() -> None:
    """Execute the page loader."""
    parser = argparse.ArgumentParser(description='Download web page')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=default_path,
        help='select folder where to download the page; default: {0}'.format(
            default_path,
        ),
    )
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    try:
        path = download(args.url, args.output)
    except (ExpectedError, requests.exceptions.RequestException) as err:
        logger.error(err)
    except Exception as err:
        logger.error('Unknown {0} error happened'.format(str(err)))
    print(SUCCESS.format(path))


if __name__ == '__main__':
    main()

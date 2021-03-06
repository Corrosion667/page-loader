#!/usr/bin/env python3
"""This program downloads a page from the network."""
import argparse
import logging
import sys
from logging import config as conf

from page_loader.download import DEFAULT_PATH, ExpectedError, download
from page_loader.logging_settings import LOGGING_CONFIG

SUCCESS = "Page was successfully downloaded into '{0}'"

conf.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def main() -> None:
    """Execute the page loader."""
    parser = argparse.ArgumentParser(description='Download web page')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=DEFAULT_PATH,
        help='select folder where to download the page; default: {0}'.format(
            DEFAULT_PATH,
        ),
    )
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    try:
        path = download(args.url, args.output)
    except ExpectedError as err:
        logger.error(err)
        sys.exit(1)
    print(SUCCESS.format(path))
    sys.exit(0)


if __name__ == '__main__':
    main()

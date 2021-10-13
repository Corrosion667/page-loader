#!/usr/bin/env python3
"""This program downloads a page from the network."""
import argparse

from page_loader.download import download


def main():
    """Execute the page loader."""
    parser = argparse.ArgumentParser(description='Download web page')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='"/app"',
        help='select folder where to download the page',
    )
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    print(
        download(args.output, args.url),
    )


if __name__ == '__main__':
    main()

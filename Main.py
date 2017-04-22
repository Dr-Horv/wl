#!/usr/bin/env python3

import argparse

from wl.wikipedia import WikipediaService


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lookup words')  # TODO, better description

    parser.add_argument('query', metavar='Query', type=str, nargs='+',
                    help='Query to search for')

    parser.add_argument('-f', '--from_lang', default='en', help='Origin language')
    parser.add_argument('-t', '--to_lang', default='sv', help='Target language')

    args = parser.parse_args()

    query = " ".join(args.query)

    result = WikipediaService.WikipediaService.search(query, from_lang=args.from_lang, to_lang=args.to_lang)

    print(result)






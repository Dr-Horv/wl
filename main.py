#!/usr/bin/env python3

import argparse

import wl.constants as constants

from wl.oxford_dictionary.OxfordDictionaryService import OxfordDictionaryService
from wl.wikipedia.WikipediaService import WikipediaService


def pretty_print_oxford(results):
    for r in results:
        print(r.get("category"))
        print("    Antonyms: {}".format(", ".join(r.get("antonyms"))))
        print("    Synonyms: {}".format(", ".join(r.get("synonyms"))))


def synonym_antonym_lookup(query):
    oxford = OxfordDictionaryService(constants.OXFORD_APP_ID, constants.OXFORD_API_KEY)
    results = oxford.lookup_anyonyms_and_synonyms(query)
    print('Query: {}'.format(query))
    pretty_print_oxford(results)


def wikipedia_translation(query, from_lang, to_lang):
    result = WikipediaService.search(query, from_lang=from_lang, to_lang=to_lang)
    print(result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lookup words')  # TODO, better description

    parser.add_argument('query', metavar='Query', type=str, nargs='+',
                    help='Query to search for')

    parser.add_argument('-f', '--from_lang', default='en', help='Origin language')
    parser.add_argument('-t', '--to_lang', default='sv', help='Target language')
    parser.add_argument('-s', action='store_true', help='Set if you want synonyms/antonyms of word')

    args = parser.parse_args()

    query = " ".join(args.query)

    if args.s:
        synonym_antonym_lookup(query)
    else:
        wikipedia_translation(query, args.from_lang, args.to_lang)









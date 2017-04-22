import requests

BASE = 'https://{lang}.wikipedia.org/w/api.php?action=query&format=json'


class WikipediaService(object):

    @staticmethod
    def search(word, from_lang, to_lang):

        resp = requests.get(
            (BASE + '&prop=langlinks&titles={title}').format(lang=from_lang, title=word))

        while resp.ok:
            dump = resp.json()
            pages = dump.get('query').get('pages')

            for k, v in pages.items():
                title = WikipediaService.check_for_lang_in_page(v, to_lang)
                if title:
                    return title

            if not dump.get('continue'):
                break

            ll = dump.get('continue').get('llcontinue')
            con = dump.get('continue').get('continue')

            url = (BASE + '&prop=langlinks&titles={title}&continue={con}&llcontinue={llcontinue}').format(
                lang=from_lang, title=word, con=con, llcontinue=ll)

            resp = requests.get(url)

    @staticmethod
    def check_for_lang_in_page(page, lang):
        langlinks = page.get('langlinks')
        for ll in langlinks:
            if ll.get('lang') == lang:
                return ll.get('*')

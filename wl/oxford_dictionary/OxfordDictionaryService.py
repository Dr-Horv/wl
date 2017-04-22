
import requests


class OxfordDictionaryService(object):

    def __init__(self, api_id, api_key):
        self.app_id = api_id
        self.api_key = api_key

    def lookup_anyonyms_and_synonyms(self, word):
        language = 'en'
        word_id = word
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'
        r = requests.get(url, headers={'app_id': self.app_id, 'app_key': self.api_key})

        if r.ok:
            list = []

            dump = r.json()
            results = dump.get('results')

            for v in results:
                entries = v.get('lexicalEntries')
                for e in entries:
                    list.append(OxfordDictionaryService.extract_lexical_entry_result(e))

            return list

    @staticmethod
    def extract_lexical_entry_result(lexical_entry):
        res = dict(
            category=lexical_entry.get('lexicalCategory'),
            synonyms=[],
            antonyms=[]
        )
        OxfordDictionaryService.populate(lexical_entry.get('entries'), res)

        return res

    @staticmethod
    def populate(entries, res):
        for e in entries:
            senses = e.get('senses')
            for sv in senses:
                synonyms = [x.get('text') for x in sv.get('synonyms', [])]
                antonyms = [x.get('text') for x in sv.get('antonyms', [])]

                res.get('synonyms').extend(synonyms)
                res.get('antonyms').extend(antonyms)




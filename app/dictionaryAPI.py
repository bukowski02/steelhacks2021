import requests
import json
import os

#for language we will be using en, and for accent we will be using gb
#for no accent enter null
def getDef(focusWord, lang, accent):
    app_id = os.eviron.get('key')
    app_key = os.eviron.get('apiId')
    if accent == 'null':
        language = lang
    else:
        language = lang+'-'+accent
    word_id = focusWord
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
    word1 = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key}).json()
    for result in word1['results']:
        for lexicalEntry in result['lexicalEntries']:
            for entry in lexicalEntry['entries']:
                for sense in entry['senses']:
                    return sense['definitions']


#!/usr/bin/python3
from random_short_url import url_generator

class urlstore():
    urldict = {}
    _file_path = 'file.json'
    def save(self, sourceUrl):
        '''
            Serializes __objects attribute to JSON file.
        '''
        urldict['sourceUrl'] = url_generator()
        with open(urlstore._file_path, mode='w', encoding="UTF8") as fd:
            json.dump(self.urldict, fd)

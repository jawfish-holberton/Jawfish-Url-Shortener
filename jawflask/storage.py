#!/usr/bin/python3
import json

class Urlstore():
    urldict = {}
    _file_path = 'file.json'
    def save(self, sourceUrl, rng_string):
        '''
            Serializes __objects attribute to JSON file.
        '''
        url_dict[rng_string] = sourceUrl
        with open(urlstore._file_path, mode='w', encoding="UTF8") as fd:
            json.dump(self.urldict, fd)

urlstore = Urlstore()

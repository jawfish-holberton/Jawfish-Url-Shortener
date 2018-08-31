#!/usr/bin/python3
import json

class Urlstore():
    urldict = {}
    _filepath = 'file.json'
    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        with open(self._filepath, mode='w', encoding="UTF8") as fd:
            json.dump(self.urldict, fd)

urlstore = Urlstore()

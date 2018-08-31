#!/usr/bin/python3
import json

class Urlstore():
    urldict = {}
    _filepath = 'file.json'

    def __init__(self):
        '''
        Load json file
        '''
        self.urldict = {}
        with open(self._filepath, mode='r', encoding="UTF8") as fd:
            self.urldict = json.load(fd)
        print ("the dictionary ", self.urldict)

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        with open(self._filepath, mode='w', encoding="UTF8") as fd:
            json.dump(self.urldict, fd)

urlstore = Urlstore()

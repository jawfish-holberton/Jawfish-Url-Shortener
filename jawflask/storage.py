#!/usr/bin/python3
import json

class Urlstore():
    urldict = {}
    deldict = {}
    _filepath = 'file.json'
    _delpath = 'dels.json'

    def __init__(self):
        '''
        Load json file
        '''
        self.urldict = {}
        self.deldict = {}
        with open(self._filepath, mode='r', encoding="UTF8") as fd:
            self.urldict = json.load(fd)
        with open(self._delpath, mode='r', encoding="UTF8") as fd:
            self.deldict = json.load(fd)
        print ("the dictionary ", self.urldict)
        print ("the deletes ", self.deldict)

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        with open(self._filepath, mode='w', encoding="UTF8") as fd:
            json.dump(self.urldict, fd)
        with open(self._delpath, mode='w', encoding="UTF8") as fd:
            json.dump(self.deldict, fd)

urlstore = Urlstore()

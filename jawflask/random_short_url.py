#!/usr/bin/python3

from storage import urlstore

import string
import random


def url_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase):
    
    url_string = ''.join(random.choice(chars) for i in range(size))
    return (url_string)
    for key in urldict:
        urldict['sourceUrl'] = url_generator()
            




if __name__ == '__main__':
    print(url_generator())

#!/usr/bin/python3


import string
import random
import sys


def url_generator():
    chars = string.ascii_uppercase + string.ascii_lowercase
    size = 6
    url_string = ''.join(random.choice(chars) for i in range(size))
    return (url_string)





if __name__ == '__main__':
    print(url_generator())

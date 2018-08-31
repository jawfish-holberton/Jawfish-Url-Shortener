#!/usr/bin/python3

import string
import random

def url_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for i in range(size))

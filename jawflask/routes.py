#!/usr/bin/python3


import flask
from flask import request

@jawfish.route('/')
@jawfish.route('/index.html')
def indexpage():
    """Dispaly basic index page"""

@jawfish.route('/newurl', methods=["POST"])
def posturl():
    """POST a url to shorten"""

@jawfish.route('/<short>')
def shorturl(shortname):
    """Return redirect to long url"""
    

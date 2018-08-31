#!/usr/bin/python3


import flask
from flask import request, abort

@jawfish.route('/')
@jawfish.route('/index.html')
def indexpage():
    """Display basic index page"""
    return render_template("index.html")

@jawfish.route('/newurl', methods=["POST"])
def posturl():
    """POST a url to shorten"""
    try:
        sourceurl = requests.json()["sourceurl"]
    except KeyError:
        abort(404)
    shrinkurl(sourceurl)

@jawfish.route('/<short>')
def shorturl(shortname):
    """Return redirect to long url"""
    try:
        return redirect(urlstore.urldict["shortname"], code = 302)
    except KeyError:
        abort(404)

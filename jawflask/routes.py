#!/usr/bin/python3


import flask
from flask import request, abort, redirect
from jawflask import jawfish
from jawflask.storage import urlstore

@jawfish.route('/')
@jawfish.route('/index.html')
def indexpage():
    """Display basic index page"""
    print("Display index")
    return render_template("index.html")


@jawfish.route('/newurl', methods=["POST"])
def posturl():
    """POST a url to shorten"""
    print("Post url to shorten")
    try:
        sourceurl = request.json()["sourceurl"]
    except KeyError:
        abort(404)
    url_generator(sourceurl)


@jawfish.route('/<short>')
def shorturl(short):
    """Return redirect to long url"""
    print("redirect to long url from: ", short)
    try:
        return redirect(urlstore.urldict[short], code = 302)
    except KeyError:
        abort(404)

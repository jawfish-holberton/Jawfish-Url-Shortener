#!/usr/bin/python3


import flask
from flask import request, abort, redirect, render_template
from jawflask import jawfish
from jawflask.storage import urlstore
from jawflask.random_short_url import url_generator

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
        sourceurl = request.get_json()
        print(sourceurl)
    except KeyError:
        abort(404)
    print(sourceurl)
    return(url_generator(sourceurl))

@jawfish.route('/deleteurl/<delshort>', methods=["DELETE"])
def delurl(delshort):
    """DELETE a url to delete"""
    print("Post url to delete")
    try:
        del urlstore.urldict[delshort]
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

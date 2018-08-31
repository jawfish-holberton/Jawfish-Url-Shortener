#!/usr/bin/python3


import flask
from flask import request, abort, redirect, send_from_directory, jsonify
from jawflask.jawfish import jawfishapp
from jawflask.storage import urlstore
from jawflask.random_short_url import url_generator

print("routes imported")

@jawfishapp.route('/')
@jawfishapp.route('/index.html')
def indexpage():
    """Display basic index page"""
    print("Display index")
    return send_from_directory("templates", "index.html")


@jawfishapp.route('/newurl', methods=["POST"])
def posturl():
    """POST a url to shorten"""
    print("Post url to shorten")
    try:
        sourceurl = request.get_json()["sourceUrl"]
        print(sourceurl)
    except KeyError:
        abort(404)
    print(sourceurl)
    return(jsonify(url_generator(sourceurl)))


def delurl(delshort):
    """DELETE a url to delete"""
    print("Post url to delete", delshort)
    try:
        print("in try")
        shorturl = urlstore.deldict[delshort]
        print("shorturl = ", shorturl)
        del urlstore.urldict[shorturl]
        del urlstore.deldict[delshort]
        urlstore.save()
        print("Saved deletion")
    except KeyError:
        return "Not Found"
    return "Deleted short url" + shorturl, 200

@jawfishapp.route('/<short>')
def shorturl(short):
    """Return redirect to long url"""
    print("redirect to long url from: ", short)
    if len(short) == 7:
        return delurl(short)
    try:
        return redirect(urlstore.urldict[short], code = 302)
    except KeyError:
        abort(404)

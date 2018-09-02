#!/usr/bin/python3


import flask
from flask import request, abort, redirect, send_from_directory, jsonify
from jawflask.jawfish import jawfishapp
from jawflask.storage import urlstore
from jawflask.random_short_url import url_generator
from requests import head

print("routes imported")

@jawfishapp.route('/')
@jawfishapp.route('/index.html')
def indexpage():
    """Display basic index page"""
    print("Display index")
    return send_from_directory("static", "index.html")


@jawfishapp.route('/newurl', methods=["POST"])
def posturl():
    """POST a url to shorten"""
    print("Post url to shorten")
    try:
        sourceurl = request.get_json()["sourceUrl"]
        print(sourceurl)

        source = head(sourceurl);
        cors_headers = source.headers.get("X-Frame-Options", None)
        is_framable = True

        if cors_headers:
            if "sameorigin" in cors_headers.lower():
                is_framable = False

        print("Previewability has been tested")
        print("Previewability:", is_framable)
        
    except KeyError:
        abort(404)

    print(sourceurl)
    return(jsonify({"shortUrl": url_generator(sourceurl),
                    "isFramable": is_framable}))


@jawfishapp.route('/deleteurl/<delshort>', methods=["DELETE"])
def delurl(delshort):
    """DELETE a url to delete"""
    print("Post url to delete")
    try:
        del urlstore.urldict[delshort]
    except KeyError:
        return "Not Found"
    return("OK")


@jawfishapp.route('/<short>')
def shorturl(short):
    """Return redirect to long url"""
    print("redirect to long url from: ", short)
    try:
        return redirect(urlstore.urldict[short], code = 302)
    except KeyError:
        abort(404)

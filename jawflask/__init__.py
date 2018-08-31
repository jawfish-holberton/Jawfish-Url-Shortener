#!/usr/bin/python3
"""Init flask app"""


from flask import Flask
from jawflask import storage


jawfish = Flask(__name__)


from jawflask import routes


#jawflask.run(host="35.221.16.149", port="80")
jawfish.run(host="localhost", port="80")

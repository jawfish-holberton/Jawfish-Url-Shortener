"""Init flask app"""

from os import getenv
from flask import Flask
from jawflask import storage


jawfishapp = Flask(__name__)


from jawflask.routes import *


if __name__ == "__main__":
    host = getenv("APP_HOST", "localhost")
    port = getenv("APP_PORT", 80)
    
    jawfishapp.run(host=host, port=int(port))

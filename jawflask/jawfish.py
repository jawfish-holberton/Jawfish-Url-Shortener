"""Init flask app"""


from flask import Flask
from jawflask import storage


jawfishapp = Flask(__name__)


from jawflask.routes import *


if __name__ == "__main__":
    #jawflask.run(host="35.221.16.149", port="80")
    jawfishapp.run(host="localhost", port="80")

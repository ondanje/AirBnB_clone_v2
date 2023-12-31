#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    return "HBNB"


if __name__ == '__main__':
    """must be listening on 0.0.0.0, port 5000"""
    app.run('0.0.0.0', port=5000)

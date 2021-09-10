#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays single line"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index_2():
    """Displays single line"""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_func(text):
    """Displays C + single line"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

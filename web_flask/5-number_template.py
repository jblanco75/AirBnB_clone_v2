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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def is_number(n):
    """display “n is a number” only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page from template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

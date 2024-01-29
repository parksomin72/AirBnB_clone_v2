#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask
from flask import render_template
from flask import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays 'C ', followed by the value of the text variable"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """Displays 'Python ', followed by the value of the text variable"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer"""
    return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
"""Displays an HTML page only if n is an integer and
indicates if it's odd or even"""
return render_template('6-number_odd_or_even.html',
number=n, result="odd" if n % 2 != 0 else "even")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

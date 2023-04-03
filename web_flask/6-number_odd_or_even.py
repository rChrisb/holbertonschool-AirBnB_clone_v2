#!/usr/bin/python3
""" Hello Flask!"""

from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_language(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_language(text=None):
    if text:
        return f"Python {escape(text.replace('_', ' '))}"
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_or_odd(n):
    if n % 2 == 0:
        return render_template(
            "6-number_odd_or_even.html", n=n, odd_even="even")
    return render_template("6-number_odd_or_even.html", n=n, odd_even="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

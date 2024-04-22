#!/usr/bin/python3
""" starting a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def holberton():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def cIsFun(text):
    modified_text = text.replace('_', ' ')
    return 'C {}'.format(modified_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonIsFun(text="is cool"):
    modified_text = text.replace('_', ' ')
    return 'Python {}'.format(modified_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

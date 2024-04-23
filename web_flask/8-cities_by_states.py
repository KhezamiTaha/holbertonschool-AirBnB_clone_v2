#!/usr/bin/python3
""" starting a Flask web application """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def jinja_template():
    return render_template('8-cities_by_states.html',
                           all_states=storage.all(State))


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown app context"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

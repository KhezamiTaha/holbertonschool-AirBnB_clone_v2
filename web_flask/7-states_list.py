#!/usr/bin/python3
""" starting a Flask web application """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    all_states = storage.all(State)
    sorted_states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', all_states=sorted_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown app context"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

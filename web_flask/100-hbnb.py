#!/usr/bin/python3
""" starting a Flask web application """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states_amenities():
    return render_template('100-hbnb.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(),
                           places=storage.all(Place).values())


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown app context"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

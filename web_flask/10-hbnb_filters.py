#!/usr/bin/python3
""" Hello Flask!"""

from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def all_states_all_amenities():
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", all_states=all_states,
                           all_amenities=all_amenities)


@app.teardown_appcontext
def teardown_handle(app):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

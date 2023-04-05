#!/usr/bin/python3
""" Hello Flask!"""

from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def all_states():
    all_states = storage.all(State)
    return render_template("8-cities_by_states.html", states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_handle(app):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

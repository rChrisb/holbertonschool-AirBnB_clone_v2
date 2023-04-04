#!/usr/bin/python3
""" Hello Flask!"""

from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_handle(app):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states_list = sorted(
        storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Show List all the states in the template Html """
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Show List all the states in the template Html """
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page like 6-index.html """
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    amenities = sorted(list(storage.all(Amenity).values()),
                       key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

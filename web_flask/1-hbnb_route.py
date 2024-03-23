#!/usr/bin/python3
"""Flask web application"""

from crypt import methods
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def hello():
    """Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False, methods=['GET'])
def hbnb():
    """Return HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

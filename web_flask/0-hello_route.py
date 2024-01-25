#!/usr/bin/python3
"""script that starts a Flask web application"""

# import Flask class from flask module
from flask import Flask

# create an instance called app of the class by passing the __name__ variable
app = Flask(__name__)

@app.route('/airbnb-onepage/')
def index():
    """display "Hello HBNB!" on the index page"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

"""
    Main program; calls the methods necessary for setting up
    the database and running the application
"""
from flask import render_template

from server.app import APP
from server.db_driver import initializeDB
from server.read_csv import read


# REPLACE THIS
@APP.route("/")
def index():
    return render_template("index.html")

@APP.route('/test')
def helloWorld():
    return "Hello World"

if __name__ == "__main__":
    initializeDB()
    read()
    APP.run()

import sqlite3
from flask import g

from run_app import app

DATABASE = '/sqlite3.db'


def getDB():
    db = getattr(g, '_database', None)
    if db is not None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def closeConnection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

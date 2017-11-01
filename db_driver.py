import sqlite3
from flask import g

from app import APP

DATABASE = 'video_games_sample.db'
SCHEMAS = [
    'vg_schema.sql',
    'ign_schema.sql'
]


def getDB():
    """
    :return: The database instance
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # makes queries return sqlite3 formatted dictionaries for ease of use
        db.row_factory = sqlite3.Row
    return db


@APP.teardown_appcontext
def closeConnection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        print("DB closed") #FOR DEBUGGING
    elif exception is not None:
        raise Exception("Database instance is empty")



def initializeDB():
    with APP.app_context():
        db = getDB()
        count = 0
        folder = "sql scripts/"
        for schema in SCHEMAS:
            with APP.open_resource(folder+schema,mode='r') as file:
                db.cursor().execute(file.read())
            db.commit()
            count += 1
        print("Committed schema to DB? ",count == len(SCHEMAS)) # FOR DEBUGGING


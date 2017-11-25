"""
    Main program; calls the methods necessary for setting up
    the database and running the application
"""


from server.app import APP
from server.db_driver import initializeDB
from server.read_csv import read

import server.routes


if __name__ == "__main__":
    initializeDB()
    read()
    APP.run()

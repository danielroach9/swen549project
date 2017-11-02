"""
    Main program; calls the methods necessary for setting up
    the database and running the application
"""
from app import APP
from db_driver import initializeDB
from read_csv import read

# REPLACE THIS
@APP.route('/')
def helloWorld():
    return "Hello World"

if __name__ == "__main__":
    initializeDB()
    read()
    APP.run()

from app import APP
from db_driver import initializeDB
@APP.route('/')
def helloWorld():
    return "Hello World"

if __name__ == "__main__":
    initializeDB()
    APP.run()

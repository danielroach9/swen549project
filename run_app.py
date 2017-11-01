from app import APP
from db_driver import initializeDB
from read_csv import readVideoGames
@APP.route('/')
def helloWorld():
    return "Hello World"

if __name__ == "__main__":
    initializeDB()
    readVideoGames()
    APP.run()

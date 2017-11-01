from db_driver import getDB
from videogames.model.VideoGameModel import VideoGameModel
from app import APP
import sys

from dao import DAOInterface

class VideoGameSalesDAO( DAOInterface):
    def __init__( self ):
        # queries
        self.selectAllQuery = "SELECT * FROM video_game_sales"
        self.selectQuery = "SELECT * FROM video_game_sales WHERE Rank=?"

        self.insertQuery = "INSERT INTO video_game_sales " \
                      "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
        self.deleteQuery = "DELETE FROM video_game_sales where Rank=?"
        self.updateQuery = "UPDATE video_game_sales SET ?=? WHERE Rank=?"

        self.lastRowCount = 0



    def selectAll( self ):
        errMsg = "Failed trying to perform SELECT ALL query for Video Game Sales - "

        data = self.query( self.selectAllQuery,eMsg=errMsg,select=True )
        return self.createVideoGames( data )

    def select( self, args):
        errMsg = "Failed trying to perform SELECT query for Video Game Sales - "

        data = self.query( self.selectQuery, args, eMsg=errMsg,select=True )
        if len(data) == 0:
            return None
        return self.createVideoGame( data[0] )

    def insert(self, args):
        errMsg = "Failed trying to perform INSERT query for Video Game Sales - "
        rowCount = self.query( self.insertQuery, args,True,errMsg )
        didInsert = rowCount == self.lastRowCount +1

        if didInsert:
            self.lastRowCount = rowCount
        return didInsert

    def delete(self, args=() ):
        errMsg = "Failed trying to perform DELETE query for Video Game Sales - "
        return self.query( self.deleteQuery, args,True,errMsg )

    def update(self, args=()):
        errMsg = "Failed trying to perform UPDATE query for Video Game Sales - "

        rowCount = self.query( self.updateQuery, args, True, errMsg )
        return rowCount == 1

    def query( self, query, args=(), select=False, commit=False, eMsg="" ):
        with APP.app_context():
            db = getDB()
            try:

                cursor = db.execute(query, args)

                if select:
                    result = cursor.fetchall()
                else:
                    result = cursor.rowcount

                if commit:
                    db.commit()

                cursor.close()
                return result

            except Exception as e:
                print(eMsg, e)
                sys.exit(1)

    def createVideoGame(self,rowData):
        return VideoGameModel(rowData)

    def createVideoGames(self,allData):
        videoGames = list(map(self.createVideoGame,allData))
        return videoGames






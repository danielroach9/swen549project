from db_driver import getDB
from videogames.model.VideoGameModel import VideoGameModel

class VideoGameSalesDAO( object ):
    def __init__( self ):
        # queries
        self.selectAllQuery = "SELECT * FROM video_game_sales"
        self.selectQuery = "SELECT * FROM video_game_sales WHERE Rank=?"

        self.insertQuery = "INSERT INTO video_games_sales " \
                      "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
        self.deleteQuery = "DELETE FROM video_game_sales where Rank=?"
        self.updateQuery = "UPDATE video_game_sales SET ?=? WHERE Rank=?"

        self.lastRowCount = 0

    def selectAll( self ):
        cursor = self.query( self.selectAllQuery )
        return self.createVideoGames( cursor.fetchall() )

    def select( self, args=()):
        cursor = self.query( self.selectQuery, args )
        return self.createVideoGame( cursor.fetchone() )

    def insert(self, args):
        cursor = self.query( self.insertQuery, args )

        didInsert = cursor.rowcount == self.lastRowCount +1

        if didInsert:
            self.lastRowCount = cursor.rowcount

        return didInsert

    def delete(self, args=() ):
        return self.query( self.deleteQuery, args )

    def update(self, args=()):
        cursor = self.query( self.updateQuery, args )
        return cursor.rowcount == 1

    def query( self, query, args=() ):
        db = getDB()
        try:

            cursor = db.execute(query, args)
            result = cursor
            cursor.close()
            return result
        except Exception as e:
            print("Failed trying to perform select all query for Video Game Sales", e)

    def createVideoGame(self,rowData):
        return VideoGameModel(rowData)

    def createVideoGames(self,allData):
        videoGames = list(map(self.createVideoGame,allData))
        return videoGames






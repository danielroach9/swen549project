"""
    This file contains the Data Access Object (DAO) for Video Game Sales

    Date - 11/2/17
    Author - Philip Bedward
"""
from .dao_interface import DAO
from model.videoGameModel import VideoGameModel


class VideoGameSalesDAO(DAO):
    """
    Data Access object for Video Game Sales
    implements all methods from the DAO parent class and
    methods to create a list of IGNReviewModels or just one IGNReviewModel
    """
    def __init__( self ):
        """
        Class Constructor
        """
        super().__init__() # DAO class constructor

        ### DEFINE CRUD QUERIES ###

        self.selectAllQuery = "SELECT * FROM video_game_sales"
        self.selectQuery = "SELECT * FROM video_game_sales WHERE Rank=?"

        self.insertQuery = "INSERT INTO video_game_sales " \
                      "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
        self.deleteQuery = "DELETE FROM video_game_sales WHERE Rank=?"
        self.updateQuery = "UPDATE video_game_sales SET ?=? WHERE Rank=?"





    def selectAll( self):
        self.errMsg = "Failed trying to perform SELECT ALL query for Video Game Sales - "

        return super().selectAll(func=self.createVideoGames)

    def select( self, args,func=None):
        self.errMsg = "Failed trying to perform SELECT query for Video Game Sales - "
        func = self.createVideoGame
        return super().select(args ,func)

    def insert(self, args):
        self.errMsg = "Failed trying to perform INSERT query for Video Game Sales - "
        return super().insert(args)

    def delete(self, args ):
        self.errMsg = "Failed trying to perform DELETE query for Video Game Sales - "
        return super().delete(args)

    def update(self, args):
        self.errMsg = "Failed trying to perform UPDATE query for Video Game Sales - "
        return super().update(args)


    def query( self, query, args=(), select=False, commit=False, eMsg="" ):
        return super().query(query ,args ,select ,commit ,eMsg)

    def createVideoGame(self ,rowData):
        """
        Create one  VideoGameModel
        :param rowData: all column values in an individual row
        :return: IGNReviewModel Object with the data found in that row
        or None
        """
        if rowData == None:
            return None
        return VideoGameModel(rowData)

    def createVideoGames(self ,allData):
        """
       Create a list of VideoGameModels
        - see: createVideoGame(rowData)
       :param allData: list of all the rows in the table
       :return: List of VideoGameModel Objects
       """
        videoGames = list(map(self.createVideoGame ,allData))
        return videoGames

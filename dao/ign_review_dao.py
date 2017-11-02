"""
    This file contains the Data Access Object for IGN Reviews

    Date - 11/2/17
    Author - Philip Bedward
"""
from .dao_interface import DAO
from model.ignReviewModel import IGNReviewModel



class IGNReviewDAO(DAO):
    """
    Data Access object for IGN Reviews
    implements all methods from the DAO parent class and
    methods to create a list of IGNReviewModels or just one IGNReviewModel
    """
    def __init__(self):
        """
            Class Constructor
        """
        super().__init__()

        ### DEFINE CRUD QUERIES ###

        self.insertQuery = "INSERT INTO ign_reviews " \
                           "VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"

        self.selectAllQuery = "SELECT * FROM ign_reviews"
        self.selectQuery = "SELECT * FROM ign_reviews WHERE ID=?"

        self.updateQuery = "UPDATE ign_reviews SET ?=? WHERE ID=?"
        self.deleteQuery = "DELETE FROM ign_reviews where ID=?"



    def selectAll(self):
        self.errMsg = "Failed trying to perform SELECT ALL query for IGN Reviews - "
        return super().selectAll(self.createIGNReviews)

    def select(self, args):
        self.errMsg = "Failed trying to perform SELECT query for IGN Reviews - "
        return super().select(args, self.createIGNReview)


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
        return super().query(query, args, select, commit, eMsg)


    def createIGNReview( self, rowData ):
        """
        Create one  IGNReviewModel
        :param rowData: all column values in an individual row
        :return: IGNReviewModel Object with the data found in that row
        or None
        """
        if rowData == None:
            return None
        return IGNReviewModel(rowData)

    def createIGNReviews(self,allData):
        """
        Create a list of IGNReviewModels
         - see: createIGNReview(rowData)
        :param allData: list of all the rows in the table
        :return: List of IGNReviewModel Objects
        """
        # maps each row in the list of rows to the createIGNReview function
        # then places the IGNReviewModel in a list
        ignReviews = list(map(self.createIGNReview,allData))
        return ignReviews


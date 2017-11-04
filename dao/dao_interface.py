"""
    This file contains the Data Access Object abstract class

    Date - 11/2/17
    Author - Philip Bedward
"""
from db_driver import getDB
from app import APP
import sys

class DAO:
    """
    Data Access object for IGN Reviews
    creates abtract methods for making queries to a given database table.

    The queries must be defined by the child class.
    """
    def __init__(self):
        self.selectAllQuery = ""
        self.selectQuery = ""

        self.insertQuery = ""
        self.deleteQuery = ""
        self.updateQuery = ""
        self.errMsg = ""
        self.lastRowCount = 0

    def selectAll(self,func):
        """
        Select All rows from a given database table (table defined by query in child class)
        :param func: Callback function that will create a list of model objects
        ** must be defined and passed by the child class **
        :return: a list of model objects
        """
        data = self.query(self.selectAllQuery, eMsg=self.errMsg, select=True)
        return func(data)

    def select(self, args,func):
        """
        Select one row from a given database table (table defined by query in child class)
        :param args: tuple containing the primary key to select
        :param func: Callback function that will create a model object
        ** must be defined and passed by the child class **
        :return: one model object
        """
        data = self.query(self.selectQuery, args, eMsg=self.errMsg, select=True)
        if len(data) == 0:
            return None
        return func(data[0])

    def insert(self, args):
        """
        Select one row from a given database table (table defined by query in child class)
        :param args: tuple containing the values to insert into the table
        :return: a boolean whether or not the value was inserted or not
        """
        rowCount = self.query(self.insertQuery, args,  eMsg=self.errMsg, commit=True)
        return rowCount == 1


    def delete(self, args):
        """
        Delete one row from a given database table (table defined by query in child class)
        :param args: tuple containing the primary key to delete
        :return: ** unsure for now **
        """
        return self.query(self.deleteQuery, args, eMsg=self.errMsg, commit=True)

    def update(self, args, props):
        """
        Select one row from a given database table (table defined by query in child class)
        :param args: tuple containing the values and the primary key to update in the
        table
        :return: a boolean whether or not the value was inserted or not
        """
        sep = "=? "
        propertiesStr = (sep.join(props) + sep)
        self.updateQuery = self.updateQuery.format(props=propertiesStr)

        rowCount = self.query(self.updateQuery, args, eMsg=self.errMsg, commit=True)
        return rowCount == 1

    def query(self, query, args=(), select=False, commit=False, eMsg=""):
        """
        Execute a given query on a database table.
        :param query: the query to be executed
        :param args: the arguments to pass into each statement
        :param select: whether it's a select clause or not
        :param commit: whether we want to save the modifications to the db or not
        :param eMsg:  the error message to print
        :return:
        """
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


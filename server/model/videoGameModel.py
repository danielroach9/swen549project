"""
    This file contains the Model Class for Video Game Sales

    Date - 11/2/17
    Author - Philip Bedward
"""
class VideoGameModel(object):
    """
    Representation of a row of data from the IGN Review Table
    """
    ONE_MILLION = 10**6 # 10^6
    def __init__(self,row):
        """
        Class Constructor
        Stores all of the column values from the given row
        :param row: all column values of a row of data
        """

        self.rank = row["Rank"]
        self.name = row["Name"]
        self.platform = row["Platform"]
        self.year = row["Year"]
        self.genre = row["Genre"]
        self.publisher = row["Publisher"]
        self.naSales = row["NA_Sales"]
        self.euSales = row["EU_Sales"]
        self.jpSales = row["JP_Sales"]
        self.otherSales = row["Other_Sales"]
        self.globalSales = row["Global_Sales"]

    ### DEFINE GETTERS ###
    def getRank(self):
        return self.rank

    def getName(self):
        return self.name

    def getPlatform(self):
        return self.platform

    def getYear(self):
        return self.year

    def getGenre(self):
        return self.genre

    def getPublisher(self):
        return self.publisher

    def getNaSales(self):
        return self.naSales * self.ONE_MILLION

    def getEuSales(self):
        return self.euSales * self.ONE_MILLION
    def getJpSales(self):
        return self.jpSales * self.ONE_MILLION
    def getOtherSales(self):
        return self.otherSales * self.ONE_MILLION

    def getGlobalSales(self):
        return self.globalSales

"""
    This file contains the Model Class for IGN Reviews

    Date - 11/2/17
    Author - Philip Bedward
"""
class IGNReviewModel:
    """
    Representation of a row of data from the IGN Review Table
    """
    def __init__(self,row):
        """
        Class Constructor
        Stores all of the column values from the given row
        :param row: all column values of a row of data
        """
        self.id = row["ID"]
        self.scorePhrase = row["Score_Phrase"]
        self.title = row["Title"]
        self.url = row["Url"]
        self.platform = row["Platform"]
        self.score = row["Score"]
        self.genre = row["Genre"]
        self.editorsChoice = row["Editors_Choice"]
        self.releaseYear = row["Release_Year"]
        self.releaseMonth = row["Release_Month"]
        self.releaseDay = row["Release_Day"]

    ### DEFINE GETTERS ###

    def getScorePhrase(self):
        return self.scorePhrase

    def getTitle(self):
        return self.title

    def getUrl(self):
        return self.url

    def getPlatform(self):
        return self.platform

    def getScore(self):
        return self.score

    def getGenre(self):
        return self.genre

    def getEditorsChoice(self):
        return self.editorsChoice

    def getReleaseYear(self):
        return self.releaseYear

    def getReleaseMonth(self):
        return self.releaseMonth

    def getReleaseDay(self):
        return self.releaseDay

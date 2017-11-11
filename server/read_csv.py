"""
    Script that reads in data from the csv files and loads them into the database

    Date - 11/2/17
    Author - Philip Bedward, Daniel Roch, Sadaf Chowdhury, Daniel Darius Cox
"""
import pandas as pd
from .dao.video_game_sales_dao import VideoGameSalesDAO

from .dao.ign_review_dao import IGNReviewDAO

import os


def readVideoGames():
    """
    Reads the video games csv data into its corresponding database table
    :return:
    """
    # TODO: Should take command line input in future
    csv = pd.read_csv(os.getcwd()+"/sample_data/Sample_Video_Game_Sales.csv")
    maxRank = csv["Rank"].max()

    vgDAO = VideoGameSalesDAO()
    for i in range(maxRank):

        frame = csv.loc[i]
        rank = int(frame["Rank"])
        name = str(frame["Name"])
        platform = str(frame["Platform"])
        year = int(frame["Year"])
        genre = str(frame["Genre"])
        publisher = str(frame["Publisher"])
        naSales = float(frame["NA_Sales"])
        euSales = float(frame["EU_Sales"])
        jpSales = float(frame["JP_Sales"])
        otherSales = float(frame["Other_Sales"])
        globalSales = float(frame["Global_Sales"])

        # TODO: when scaling up, find out to perform batch SELECT and INSERT using execute many
        attrs = (rank, name, platform, year, genre, publisher, naSales, euSales, jpSales, otherSales, globalSales)
        exists = vgDAO.select( (rank,) ) != None

        if not exists:
            vgDAO.insert( attrs )

def readIGNReviews():
    """
    Reads the ign review csv data into its corresponding database table
    :return:
    """
    # TODO: Should take command line input in future
    csv = pd.read_csv(os.getcwd()+"/sample_data/Sample_IGN_Reviews.csv")
    count = len(csv.index)

    ignDAO = IGNReviewDAO()
    convertToBool = lambda x: False if x =="N" else True
    for i in range(count):

        frame = csv.loc[i]
        scorePhrase = str(frame["score_phrase"])
        title = str(frame["title"])
        url = str(frame["url"])
        platform = str(frame["platform"])
        score = int(frame["score"])
        genre = str(frame["genre"])
        editorsChoice = convertToBool(frame["editors_choice"])
        year = int(frame["release_year"])
        month = int(frame["release_month"])
        day = int(frame["release_day"])

        # TODO: when scaling up, find out how to perform batch SELECT and INSERT this using execute many
        attrs = (i , scorePhrase, title, url, platform, score, genre, editorsChoice, year, month, day )
        exists = ignDAO.select( (i,) ) != None

        if not exists:
            ignDAO.insert( attrs )



def read():
    """
    read in both CSVs
    :return:
    """
    readVideoGames()
    readIGNReviews()




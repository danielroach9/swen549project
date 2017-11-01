import pandas as pd
from videogames.dao.video_game_sales_dao import VideoGameSalesDAO

def readVideoGames():
    csv = pd.read_csv("sample data/Sample Video Game Sales.csv")
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

        attrs = (rank, name, platform, year, genre, publisher, naSales, euSales, jpSales, otherSales, globalSales)
        exists = vgDAO.select( (rank,) ) != None

        if not exists:

            vgDAO.insert( attrs )


    





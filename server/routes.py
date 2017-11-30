from server.dao.video_game_sales_dao import VideoGameSalesDAO
from server.dao.ign_review_dao import IGNReviewDAO
from json import loads, dumps
from server.app import APP
from flask import render_template
from flask import request

@APP.route("/")
def index():
    return render_template("index.html")

@APP.route('/test')
def helloWorld():
    return "Hello World"

@APP.route("/globalData")
def retrieveScoresAndSales():
    scoreSales = []
    ignDao = IGNReviewDAO()
    vgDao = VideoGameSalesDAO()
    videoGames = vgDao.selectAll()

    reviews = ignDao.selectAll()
    reviewTitles = set(map(lambda x: x.getTitle().lower(),reviews))

    vgTitles = set(map(lambda y: y.getName().lower(),videoGames))

    titles = reviewTitles.intersection(vgTitles)

    i=0
    j = 0
    vgTitles = list(vgTitles)
    reviewTitles = list(reviewTitles)
    for title in titles:
        i = 0
        j = 0

        while i < len(reviewTitles) and reviewTitles[i] != title:
            i +=1

        while j < len(vgTitles) and vgTitles[j] != title:
            j += 1

        if i < len(reviewTitles) and j < len(vgTitles):
            col = [reviews[i].getScore(),videoGames[j].getGlobalSales()]
            scoreSales.append(col)


    context = {"scoreSales":scoreSales}
    return dumps(context)

@APP.route("/filterData",methods=["POST"])
def getfilteredData():
    data = loads(request.get_data())
    filters = data.get("filters")
    print(filters)
    filteredData = filterRegionData(filters[0].strip("Sales").strip())

    return dumps({"filteredData":filteredData})

def filterRegionData(region):
    GLOBAL = "global"
    JAPAN = "japan"
    EURO = "european"
    NAM = "north america"

    methodName = ""
    region = region.lower()
    if region == GLOBAL:
        methodName = "getGlobalSales"
    elif region == JAPAN:
        methodName = "getJapSales"
    elif region == EURO:
        methodName = "getJapSales"
    elif region == NAM:
        methodName = "getNaSales"
    else:
        methodName = "getOtherSales"

    return getRegionData(methodName)


def getRegionData(regionFunc):
    scoreSales = []
    ignDao = IGNReviewDAO()
    vgDao = VideoGameSalesDAO()
    videoGames = vgDao.selectAll()

    reviews = ignDao.selectAll()
    reviewTitles = set(map(lambda x: x.getTitle().lower(), reviews))

    vgTitles = set(map(lambda y: y.getName().lower(), videoGames))

    titles = reviewTitles.intersection(vgTitles)


    vgTitles = list(vgTitles)
    reviewTitles = list(reviewTitles)
    for title in titles:
        i = 0
        j = 0

        while i < len(reviewTitles) and reviewTitles[i] != title:
            i += 1

        while j < len(vgTitles) and vgTitles[j] != title:
            j += 1

        if i < len(reviewTitles) and j < len(vgTitles):
            func = getattr(videoGames[j], regionFunc)
            col = [reviews[i].getScore(), func()]
            scoreSales.append(col)

    return scoreSales

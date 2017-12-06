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
    # genres1 = set()
    genres = set()
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
            # genres1.add(reviews[i].getGenre())
            genres.add(videoGames[i].getGenre())
            scoreSales.append(col)


    context = {"scoreSales":scoreSales,"genres":list(genres)}
    return dumps(context)

@APP.route("/filterData",methods=["POST"])
def getfilteredData():
    data = loads(request.get_data())
    filters = data.get("filters")
    print(filters)
    region = filters[0].strip("Sales").strip()
    genre = filters[1]
    score = filters[2]
    filteredData = filterData(region,genre,score)

    return dumps({"filteredData":filteredData})

def filterData(region,genre,score):

    JAPAN = "japan"
    EURO = "european"
    NAM = "north america"
    OTHER = "other"
    ALL = "all"
    methodName = ""
    region = region.lower()

    allScores = False
    allGenres = False
    if region == OTHER:
        methodName = "getOtherSales"
    elif region == JAPAN:
        methodName = "getJapSales"
    elif region == EURO:
        methodName = "getJapSales"
    elif region == NAM:
        methodName = "getNaSales"
    else:
        methodName = "getGlobalSales"

    if genre.lower() == ALL:
        allGenres = True
    try:
        score = int(score)
    except Exception as e:
        allScores = True
    print(allScores)
    print(allGenres)
    if allScores and allGenres:
        return getRegionData(methodName)

    elif not allScores and allGenres:
        print("here")
        return getRegionData(methodName,score=score)
    elif allScores and not allGenres:
        return getRegionData(methodName,genre=genre)
    else:
        return getRegionData(methodName,genre,score)

#modify this method to work with score and genre
def getRegionData(regionFunc,genre=None,score=None):
    print("enter function")
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

            salesFunc = getattr(videoGames[j], regionFunc)
            currScore = reviews[i].getScore()

            print("param : " + str(score) + " game score " + str(currScore))
            scoreToAdd = None
            numSales = None
            if score == None and genre == None:
                print("just sales")
                scoreToAdd = currScore
                numSales = salesFunc()
            if score != None and genre != None:
                print("score and genre")
                if videoGames[j].getGenre() == genre:
                    if score == currScore:
                        scoreToAdd = currScore
                        numSales = salesFunc()
            elif score != None and score == currScore:
                print("score")
                scoreToAdd = currScore
                numSales = salesFunc()
            elif genre != None and genre == videoGames[j].getGenre():
                print("genre")
                scoreToAdd = currScore
                numSales = salesFunc()

            if scoreToAdd and numSales:
                col = [scoreToAdd, numSales]
                scoreSales.append(col)

    return scoreSales

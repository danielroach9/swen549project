from server.dao.video_game_sales_dao import VideoGameSalesDAO
from server.dao.ign_review_dao import IGNReviewDAO
from json import dumps
from server.app import APP
from flask import render_template

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

    # titles = reviewTitles.intersection(vgTitles)
    # print(titles)
    # lst = list(map(lambda a,b: [a] if a.getTitle().lower() == b else None,reviews,titles))
    # print(lst)
    # lst1 = list(filter(lambda x: x != None, lst))
    #
    # lst2 = list(map(lambda a,b: [a] if a.getName().lower() == b else None,videoGames,titles))
    # lst2 = list(filter(lambda x: x != None, lst2))






    print(scoreSales)
    context = {"scoreSales":scoreSales}
    return dumps(context)




from server.dao.ign_review_dao import IGNReviewDAO
from server.db_driver import initializeDB
from server.model.ignReviewModel import IGNReviewModel
from server.read_csv import read


def setup():
    initializeDB()
    read()
    global dao
    dao = IGNReviewDAO()

def testSelect():

    model = dao.select((1,))
    assert isinstance(model,IGNReviewModel) == True

def testSelectAll():
    models = dao.selectAll()
    assert len(models) == 100

def testInsert():
    isInserted = dao.insert((101,"Great","NHL 13","/games/nhl-13/xbox-360-128182","Xbox 360",8.5,"Sports","N",2012,9,11))
    model = dao.select((101,))
    assert model != None
    assert model.scorePhrase == "Great"
    assert isInserted == True

def testUpdate():
    newTitle = "test"
    props = ("title",)
    isUpdated = dao.update((newTitle,1),props)
    model = dao.select((1,))
    assert isUpdated == True
    assert model.title == newTitle

def testDelete():
    isDeleted = dao.delete((101,))
    assert isDeleted == True

def testDoubleInsert():
    isInserted = dao.insert((101, "Great", "NHL 13", "/games/nhl-13/xbox-360-128182", "Xbox 360", 8.5, "Sports", "N", 2012, 9, 11))
    assert isInserted == True
    isInserted = dao.insert((101, "Great", "NHL 13", "/games/nhl-13/xbox-360-128182", "Xbox 360", 8.5, "Sports", "N", 2012, 9, 11))
    assert isInserted == False


if __name__ == "__main__":
    setup()
    testSelectAll()
    testSelect()
    testUpdate()
    testInsert()
    testDelete()

    testDoubleInsert()
    testDelete()
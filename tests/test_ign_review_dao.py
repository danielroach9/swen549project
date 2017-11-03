from dao.ign_review_dao import IGNReviewDAO
from db_driver import initializeDB
from read_csv import read
from model.ignReviewModel import IGNReviewModel

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
    assert len(models) == 101

def testInsert():
    isInserted = dao.insert((102,"Great","NHL 13","/games/nhl-13/xbox-360-128182","Xbox 360",8.5,"Sports","N",2012,9,11))
    assert isInserted == True

def testUpdate():
    newTitle = "test"
    props = ("title",)
    isUpdated = dao.update(props,(newTitle,1))
    model = dao.select((1,))
    assert isUpdated == True
    assert model.title == newTitle

def testDelete():
    pass


if __name__ == "__main__":
    setup()
    testInsert

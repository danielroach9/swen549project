from server.dao.video_game_sales_dao import VideoGameSalesDAO
from server.db_driver import initializeDB
from server.model.videoGameModel import VideoGameModel
from server.read_csv import read


def setup():
    initializeDB()
    read()
    global dao
    dao = VideoGameSalesDAO()

def testSelect():
    model = dao.select((1,))
    assert isinstance(model,VideoGameModel) == True

def testSelectAll():
    models = dao.selectAll()
    assert len(models) == 100

def testInsert():
    isInserted = dao.insert((101,"Wii Sports","Wii",2006,"Sports","Nintendo",41.49,29.02,3.77,8.46,82.74))
    assert isInserted == True

def testUpdate():
    newName = "test"
    props = ("name",)
    isUpdated = dao.update((newName,1),props)
    model = dao.select((1,))
    assert isUpdated == True
    assert model.name == newName

def testDelete():
    isDeleted = dao.delete((101,))
    assert isDeleted == True

def testDoubleInsert():
    isInserted = dao.insert((101, "Wii Sports", "Wii", 2006, "Sports", "Nintendo", 41.49, 29.02, 3.77, 8.46, 82.74))
    assert isInserted == True
    isInserted = dao.insert((101, "Wii Sports", "Wii", 2006, "Sports", "Nintendo", 41.49, 29.02, 3.77, 8.46, 82.74))
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

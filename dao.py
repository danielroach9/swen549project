class DAOInterface(object):
    def __init__(self):
        self.selectAll = ""
        self.selectAllQuery = ""
        self.selectQuery = ""

        self.insertQuery = ""
        self.deleteQuery = ""
        self.updateQuery = ""

        self.lastRowCount = 0

    def selectAll(self):
        raise NotImplementedError

    def select(self, args):
        raise NotImplementedError

    def insert(self, args):
        raise NotImplementedError


    def delete(self, args=()):
        raise NotImplementedError

    def update(self, args=()):
        raise NotImplementedError

    def query(self, query, args=(), select=False, commit=False, eMsg=""):
        raise NotImplementedError


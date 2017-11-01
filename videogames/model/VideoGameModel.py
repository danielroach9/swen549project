class VideoGameModel(object):
    ONE_MILLION = 10**6 # 10^6
    def __init__(self,row):


        self.rank = row["Rank"]
        self.name = row["Name"]
        self.platform = row["Platform"]
        self.year = row["Year"]
        self.genre = row["Genre"]
        self.publisher = row["Publisher"]
        self.naSales = row["NA_Sales"]
        self.euSales = row["EU_Sales"]
        self.jpSales = row["JP_Sales"]
        self.otherSales = row["Other_Sales"]
        self.globalSales = row["Global_Sales"]


    def getRank(self):
        return self.rank

    def getName(self):
        return self.name

    def getPlatform(self):
        return self.platform

    def getYear(self):
        return self.year

    def getGenre(self):
        return self.genre

    def getPublisher(self):
        return self.publisher

    def getNaSales(self):
        return self.naSales * self.ONE_MILLION

    def getEuSales(self):
        return self.euSales * self.ONE_MILLION
    def getJpSales(self):
        return self.jpSales * self.ONE_MILLION
    def getOtherSales(self):
        return self.otherSales * self.ONE_MILLION

    def getGlobalSales(self):
        return self.globalSales * self.ONE_MILLION

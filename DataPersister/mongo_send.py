import pymongo


class CollectionPlacer:
    def __init__(self,uri,DB,collection):
        self.connection = pymongo.MongoClient(uri)
        self.DB = self.connection[DB]
        self.collection = self.DB[collection]

    def insert(self,document):
        self.collection.insert_one(document)
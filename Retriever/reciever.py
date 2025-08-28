import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

class CollectionFetcher:
    def __init__(self,collection):
        self.USER = os.getenv('USER')
        self.PASS = os.getenv('PASS')
        self.DBNAME = os.getenv('DBNAME')
        self.connection = pymongo.MongoClient(f'mongodb+srv://{self.USER}:{self.PASS}@cluster0.6ycjkak.mongodb.net/')
        self.DB = self.connection[self.DBNAME]

        self.collection = self.DB[collection]

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

class CollectionFetcher:
    def __init__(self,collection):
        self.USER = os.getenv('USER',default='IRGC_NEW')
        self.PASS = os.getenv('PASS',default='iran135')
        self.DBNAME = os.getenv('DBNAME',default='IranMalDB')
        self.connection = pymongo.MongoClient(f'mongodb+srv://{self.USER}:{self.PASS}@cluster0.6ycjkak.mongodb.net/')
        self.DB = self.connection[self.DBNAME]
        self.collection = self.DB[collection]

a = CollectionFetcher('tweets')
print(a.collection.find_one())
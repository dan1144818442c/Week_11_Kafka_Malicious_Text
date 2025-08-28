import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient

def mongo(database_name:str,collection_name:str):
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client[database_name]
        collection = db[collection_name]
        all_documents = collection.find({})
        client.close()
        return all_documents
    except Exception as e :
        return {"Database reading error:":e}

app = FastAPI()
@app.get("/{collection_name}")
async def root(collection_name:str):
    all_documents =mongo("tweet_organizer",f"tweets_{collection_name}")
    return all_documents


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)


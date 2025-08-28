import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient

def serialize_document(doc):
    doc["_id"] = str(doc["_id"])  # ObjectId -> string
    return doc

def mongo(database_name:str,collection_name:str):
    try:
        client = MongoClient('mongodb://mongodb:27017')
        db = client[database_name]
        collection = db[collection_name]
        all_documents = list(collection.find({}))
        client.close()
        return [serialize_document(doc) for doc in all_documents]
    except Exception as e :
        return {"Database reading error:":str(e)}

app = FastAPI()
@app.get("/{collection_name}")
async def root(collection_name:str):
    all_documents =mongo("tweet_organizer",f"tweets_{collection_name}")
    return all_documents


# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)

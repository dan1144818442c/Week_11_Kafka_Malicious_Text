from fastapi import FastAPI
from mongo_dal.dal import MongoLoad
import uvicorn
app= FastAPI(title="Data Loader API (MongoDB)")



@app.get("/listening")
async def get_data():
    event = consumer_with_auto_commit('a' , 'data_kafka_project')

    return



@app.get("/get_all")
async  def get_all_data():
    dal = MongoLoad("data_kafka_project")
    col_i = dal.db['a']
    col_not_i = dal.db['b']
    return (dal.get_info(col_i) ,   dal.get_info(col_not_i))

# if __name__ == "__main__":
#
#     uvicorn.run(app, host="localhost", port=8002)




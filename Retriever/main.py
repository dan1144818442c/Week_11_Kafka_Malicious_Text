from kafka_pro import Produce
from reciever import CollectionFetcher
import pymongo
import time

kafka = Produce()

col = CollectionFetcher('tweets')

def topic_name(doc):
    if doc['Antisemitic'] == 1:
        return 'raw_tweets_antisemitic'
    else:
        return 'raw_tweets_not_antisemitic'

def str_change(doc,field):
    doc[field] = str(doc[field])

def program_run_100_per_min(kafka_publisher,collection_fetch,sort_by,list_fields_str = None):
    skip_amount = 0
    while True:
        count = 0
        for document in collection_fetch.collection.find().sort(sort_by, pymongo.DESCENDING).limit(100).skip(skip_amount):
            count += 1
            if list_fields_str is not None:
                for field in list_fields_str:
                    str_change(document,field)
            kafka_publisher.publish_message(topic=topic_name(document), message=document)
        skip_amount += count
        time.sleep(60)


if __name__ == '__main__':

    program_run_100_per_min(kafka,col,'CreateDate',['_id','CreateDate'])

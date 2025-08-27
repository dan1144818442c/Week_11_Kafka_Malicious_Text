from Tools.kafka_producer import Produce
from reciever import CollectionFetcher


a = Produce()

b = CollectionFetcher('tweets')

def topic_name(doc):
    if doc['Antisemitic'] == 1:
        return 'raw_tweets_antisemitic'
    else:
        return 'raw_tweets_not_antisemitic'

for document in b.collection.find():
    document['_id'] = str(document['_id'])
    document['CreateDate'] = str(document['CreateDate'])
    print(document)
    a.publish_message(topic=topic_name(document),message=document)
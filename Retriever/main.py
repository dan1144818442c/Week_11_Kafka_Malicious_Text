from kafka_pro import Produce
from reciever import CollectionFetcher


a = Produce()

b = CollectionFetcher('tweets')

def topic_name(doc):
    if doc['Antisemitic'] == 1:
        return 'raw_tweets_antisemitic'
    else:
        return 'raw_tweets_not_antisemitic'

for document in b.collection.find():
    print('a')
    a.publish_message(topic=topic_name(document),message=str(document))


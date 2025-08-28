from kafka_con import Subscriber
from mongo_send import CollectionPlacer

subscriber = Subscriber(topic=['enriched_preprocessed_tweets_antisemitic','enriched_preprocessed_tweets_not_antisemitic'])
mongo_anti = CollectionPlacer('mongodb://localhost:27017','tweet_organizer','tweets_antisemitic')
mongo_non_anti = CollectionPlacer('mongodb://localhost:27017','tweet_organizer','tweets_not_antisemitic')

if __name__ == '__main__':

    for message in subscriber.consumer:
        if message.topic == 'enriched_preprocessed_tweets_antisemitic':
            mongo_anti.insert(message.value)
        else:
            mongo_non_anti.insert(message.value)




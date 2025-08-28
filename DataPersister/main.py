from Tools.kafka_consumer import Subscriber
from DataPersister.mongo_send import CollectionPlacer

subscriber = Subscriber(topic=['enriched_preprocessed_tweets_antisemitic','enriched_preprocessed_tweets_not_antisemitic'])
mongo_anti = CollectionPlacer('mongodb://mongodb:27017','tweet_organizer','tweets_antisemitic')
mongo_non_anti = CollectionPlacer('mongodb://mongodb:27017','tweet_organizer','tweets_not_antisemitic')

if __name__ == '__main__':

    for message in subscriber.consumer:
        if message.topic == 'enriched_preprocessed_tweets_antisemitic':
            print(message.value)
            mongo_anti.insert(message.value)
        else:
            print(message.value)
            mongo_non_anti.insert(message.value)
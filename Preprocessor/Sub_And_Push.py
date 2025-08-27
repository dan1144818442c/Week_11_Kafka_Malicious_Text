from Tools import kafka_consumer , kafka_producer, cleaner
import ast

class Preprocessor:

    def __init__(self , topic_a_to_listen, topic_b_to_listen):
        self.con_a = kafka_consumer.Subscriber(topic_a_to_listen).consumer
        self.con_b = kafka_consumer.Subscriber(topic_b_to_listen).consumer
        self.pub = kafka_producer.Produce()


    @staticmethod
    def add_clean_text_and_send(topic_to_send ,consumer , publisher:kafka_producer.Produce):
        for message in consumer:
            dic_ = message.value
            text = dic_['text']
            dic_['clean_text'] = cleaner.Cleaner.activate_all_functions(text)
            publisher.publish_message(topic_to_send , dic_)






p = Preprocessor('raw_tweets_antisemitic' , 'raw_tweets_not_antisemitic')
Preprocessor.add_clean_text_and_send('preprocessed_tweets_antisemitic' ,consumer= p.con_a ,publisher= p.pub)
Preprocessor.add_clean_text_and_send('preprocessed_tweets_not_antisemitic' ,consumer= p.con_b ,publisher= p.pub)

from Tools import kafka_consumer , kafka_producer, cleaner

class Preprocessor:

    def __init__(self , topic_a_to_listen, topic_b_to_listen):
        self.con_a = kafka_consumer.Subscriber(topic_a_to_listen)
        self.con_b = kafka_consumer.Subscriber(topic_b_to_listen)
        self.pub = kafka_producer.Produce()


    @staticmethod
    def add_clean_text_and_send(topic_to_send ,consumer , publisher:kafka_producer.Produce):
        for message in consumer:
            dic_ =  message.value
            print(dic_)
            text = dic_['original_text']
            dic_['clean_text'] = cleaner.Cleaner.activate_all_functions(text)
            publisher.publish_message(topic_to_send , dic_)







# a , b = Preprocessor.creat_consumer_for_to_topic("raw_tweets_antisemitic" , "raw_tweets_not_antisemitic")

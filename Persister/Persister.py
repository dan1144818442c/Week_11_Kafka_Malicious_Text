from Tools import kafka_producer,kafka_consumer

class Persistor:
    def __init__(self , topic_a_to_listen, topic_b_to_listen):
        self.con_a = kafka_consumer.Subscriber(topic_a_to_listen)
        self.con_b = kafka_consumer.Subscriber(topic_b_to_listen)
        self.pub = kafka_producer.Produce()


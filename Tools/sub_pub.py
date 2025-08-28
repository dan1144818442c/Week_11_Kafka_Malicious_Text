from  Tools import kafka_consumer ,kafka_producer

def sub_and_pub( topic_a_to_listen, topic_b_to_listen):
    con = kafka_consumer.Subscriber(topic=[topic_a_to_listen, topic_b_to_listen]).consumer
    pub = kafka_producer.Produce()
    return con,pub


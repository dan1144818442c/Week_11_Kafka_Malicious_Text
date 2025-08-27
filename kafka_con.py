from kafka import KafkaConsumer
import json

class Subscriber:
    def __init__(self,topic):
        self.consumer = KafkaConsumer(topic,
            value_deserializer=lambda m: json.loads(m.decode('ascii')),
            bootstrap_servers=["localhost:9092"])
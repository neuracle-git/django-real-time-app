from kafka import KafkaProducer
import json
from django.conf import settings

## 1 bestest method

# class KafkaProducerSingleton:
#     _instance = None
#     _producer = None

#     def __new__(cls, *args, **kwargs):
#         """Override the __new__ method to ensure only one instance is created."""
#         if not cls._instance:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             cls._producer = KafkaProducer(
#                 bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
#                 value_serializer=lambda v: json.dumps(v).encode('utf-8'),
#                 retries=5,  # Retry configuration
#                 batch_size=16384,  # Batch size configuration
#             )
#         return cls._instance

#     def send_message(self, topic, data):
#         """Method to send message to Kafka."""
#         if self._producer:
#             self._producer.send(topic, data)
#             self._producer.flush()
#             print(f"Message sent to topic {topic}: {data}")


## 2 bestest method

class KafkaMessageProducer:

    def __init__(self,KAFKA_BOOTSTRAP_SERVER,KAFKA_TOPIC):
        self.server = KAFKA_BOOTSTRAP_SERVER
        self.topic = KAFKA_TOPIC
        self.producer = KafkaProducer(
        bootstrap_servers=self.server,
        value_serializer = lambda v: json.dumps(v).encode('utf-8')
    )
        
    def send_message(self,data):
        self.producer.send(self.topic,data)
        self.producer.flush()
    
    def close(self):
        self.producer.close()


## 3 bestest method

def send_message_to_kafka(data):
    producer = KafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
        value_serializer = lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(settings.KAFKA_TOPIC,data)
    producer.flush()
    print("messgae sent to kafka:", data)
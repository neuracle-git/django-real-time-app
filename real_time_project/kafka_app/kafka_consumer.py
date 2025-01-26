from kafka import KafkaConsumer
import json
from django.conf import settings

def consume_messages():
    consumer = KafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Listening for messages..........")
    for message in consumer:
        print(f"received {message.value}")
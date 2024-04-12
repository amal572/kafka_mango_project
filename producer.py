from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

topic_name = 'my_topic'

# Send messages to Kafka
for i in range(10):
    message = {"message": f"Message {i}"}
    producer.send(topic_name, value=message)
    time.sleep(1)  # Simulate some delay
    print(f"Sent message: {message}")

producer.close()

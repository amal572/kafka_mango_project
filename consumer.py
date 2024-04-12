from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer('my_topic', bootstrap_servers='kafka:9092', auto_offset_reset='earliest', enable_auto_commit=True, group_id='my_group', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
try:
    mongo_client = MongoClient('mongodb://root:example@mongodb:27017/')
    #print(mongo_client)
    mongo_db = mongo_client['test_database']
    #print(mongo_db)
    mongo_collection = mongo_db['test_collection']
    #print(mongo_collection)

    for message in consumer:
        message_value = message.value
        print(f"Received message: {message_value}")
        print('yes')
        # Insert message into MongoDB
        mongo_collection.insert_one(message_value)
    print("Successfully connected to MongoDB")
except Exception as e:
    # Print an error message if there's an exception
    print("Error connecting to MongoDB:", e)

consumer.close()

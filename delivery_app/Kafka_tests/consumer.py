from kafka import KafkaConsumer

consumer = KafkaConsumer('order')
for message in consumer:
    print (message)
 
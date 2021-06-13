from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:29092')
# producer.send('order',key=b'Producer tá funcionando', value='Certin')
try:
    producer.send('order', key=b'message-two', value=b'This is Kafka-Python')
except:
    print("Deu ruim")


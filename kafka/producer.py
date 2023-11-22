from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Convert string to bytes using encode()
message = 'Hello, World!'.encode('utf-8')
producer.send('first_kafka_topic', value=message)

producer.flush()
producer.close()


from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')
num_messages = 1000
start_time = time.time()

for i in range(num_messages):
    message = f'Hello, World! {i}'.encode('utf-8')
    producer.send('first_kafka_topic', value=message)

producer.flush()
end_time = time.time()
producer.close()

elapsed_time = end_time - start_time
print(f"Sent {num_messages} messages in {elapsed_time:.2f} seconds.")

from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('first_kafka_topic',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest')

batch_size = 1000
num_messages_consumed = 0
start_time = time.time()

for message in consumer:
    num_messages_consumed += 1

    if num_messages_consumed % batch_size == 0:
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(f"Consumed {batch_size} messages in {elapsed_time:.2f} seconds.")
        start_time = current_time  # Reset the start time for the next batch

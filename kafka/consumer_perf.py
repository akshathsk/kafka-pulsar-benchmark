from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('first_kafka_topic',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest')

batch_size = 10000000
num_messages_consumed = 0
start_time_ns = time.perf_counter_ns() 

for message in consumer:
    num_messages_consumed += 1

    if num_messages_consumed % batch_size == 0:
        current_time_ns = time.perf_counter_ns()  
        elapsed_time_ns = current_time_ns - start_time_ns  
        print(f"Consumed {batch_size} messages in {elapsed_time_ns} nanoseconds.")
        start_time_ns = current_time_ns  

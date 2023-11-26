from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')
num_messages = 10000000
start_time_ns = time.perf_counter_ns() 

for i in range(num_messages):
    message = f'Hello, World! {i}'.encode('utf-8')
    producer.send('first_kafka_topic', value=message)

producer.flush()
end_time_ns = time.perf_counter_ns()  
producer.close()

elapsed_time_ns = end_time_ns - start_time_ns  
print(f"Sent {num_messages} messages in {elapsed_time_ns} nanoseconds.")

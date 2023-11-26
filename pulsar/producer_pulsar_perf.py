import pulsar
import time

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

num_messages = 10000000
start_time_ns = time.perf_counter_ns()  

for i in range(num_messages):
    producer.send((f'hello-pulsar-{i}').encode('utf-8'))

client.close()
end_time_ns = time.perf_counter_ns()  

elapsed_time_ns = end_time_ns - start_time_ns  
print(f"Sent {num_messages} messages in {elapsed_time_ns} nanoseconds.")

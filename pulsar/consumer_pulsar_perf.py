import pulsar
import time

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', subscription_name='my-sub')

batch_size = 10000000
num_messages_consumed = 0
start_time_ns = time.perf_counter_ns()  

while True:
    msg = consumer.receive()
    consumer.acknowledge(msg)
    num_messages_consumed += 1

    if num_messages_consumed % batch_size == 0:
        current_time_ns = time.perf_counter_ns() 
        elapsed_time_ns = current_time_ns - start_time_ns  
        print(f"Consumed {batch_size} messages in {elapsed_time_ns} nanoseconds.")
        start_time_ns = current_time_ns  

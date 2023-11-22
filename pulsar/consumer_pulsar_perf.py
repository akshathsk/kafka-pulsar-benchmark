import pulsar
import time

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', subscription_name='my-sub')

batch_size = 1000
num_messages_consumed = 0
start_time = time.time()

while True:
    msg = consumer.receive()
    consumer.acknowledge(msg)
    num_messages_consumed += 1

    if num_messages_consumed % batch_size == 0:
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(f"Consumed {batch_size} messages in {elapsed_time:.2f} seconds.")
        start_time = current_time  # Reset the start time for the next batch

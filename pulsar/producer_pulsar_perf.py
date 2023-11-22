import pulsar
import time

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

num_messages = 1000
start_time = time.time()

for i in range(num_messages):
    producer.send((f'hello-pulsar-{i}').encode('utf-8'))

client.close()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Sent {num_messages} messages in {elapsed_time:.2f} seconds.")

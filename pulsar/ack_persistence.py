import pulsar
import time


# Producer: The send method can be synchronous or asynchronous, affecting how acknowledgements are handled.
# Consumer: The acknowledge method controls how messages are acknowledged.

def produce_and_consume_messages():
    client = pulsar.Client('pulsar://localhost:6650')

    # Producer
    producer = client.create_producer('my-topic')
    start_time = time.time()
    for i in range(100):
        producer.send((f'Message {i}').encode('utf-8'))
    end_time = time.time()
    print(f"Producing 100 messages took {end_time - start_time:.2f} seconds")

    # Consumer
    consumer = client.subscribe('my-topic', subscription_name='my-sub')
    start_time = time.time()
    for i in range(100):
        msg = consumer.receive()
        consumer.acknowledge(msg)
    end_time = time.time()
    print(f"Consuming and acknowledging 100 messages took {end_time - start_time:.2f} seconds")

    client.close()

# Example usage
produce_and_consume_messages()

import pulsar
import time


# Producer: The send method can be synchronous or asynchronous, affecting how acknowledgements are handled.
# Consumer: The acknowledge method controls how messages are acknowledged.

def produce_and_consume_messages():
    client = pulsar.Client('pulsar://localhost:6650')

    # Producer
    producer = client.create_producer('my-topic')
    start_time_ns = time.perf_counter_ns()
    for i in range(100):
        producer.send((f'Message {i}').encode('utf-8'))
    end_time_ns = time.perf_counter_ns()
    print(f"Producing 100 messages took {end_time_ns - start_time_ns} nanoseconds")

    # Consumer
    consumer = client.subscribe('my-topic', subscription_name='my-sub')
    start_time_ns = time.perf_counter_ns()
    for i in range(100):
        msg = consumer.receive()
        consumer.acknowledge(msg)
    end_time_ns = time.perf_counter_ns()
    print(f"Consuming and acknowledging 100 messages took {end_time_ns - start_time_ns} nanoseconds")

    client.close()

# Example usage
produce_and_consume_messages()

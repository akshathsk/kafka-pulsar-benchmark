import pulsar
import time
import json
import string
import random

BATCH_SIZE = 1000  # number of messages to produce and consume in a batch

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic-1')

def generate_random_string(size):
    """Generate a random string of given size."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def produce_messages(payload_size):
    print(f"Producing {BATCH_SIZE} messages of size: {payload_size} bytes...")
    start_time = time.time()
    for _ in range(BATCH_SIZE):
        random_message = generate_random_string(payload_size)
        message_payload = {
            'message': random_message,
            'timestamp': time.time()
        }
        message_bytes = json.dumps(message_payload).encode('utf-8')
        producer.send(message_bytes)
    end_time = time.time()
    return end_time - start_time

def safe_json_deserializer(m):
    try:
        return json.loads(m.decode('utf-8'))
    except json.JSONDecodeError:
        print("Failed to decode message: ", m)
        return None

consumer = client.subscribe('my-topic-1', subscription_name='my-sub')

def consume_messages():
    print(f"Consuming {BATCH_SIZE} messages...")
    consumed_count = 0
    start_time = time.time()
    while consumed_count < BATCH_SIZE:
        msg = consumer.receive(timeout_millis=10000)
        if msg:
            consumed_count += 1
            print(f"Consumed {consumed_count} messages so far...")
            consumer.acknowledge(msg)
    end_time = time.time()
    return end_time - start_time

def main():
    payload_sizes = [10, 100, 1000, 10_000, 100_000]

    for size in payload_sizes:
        produce_time = produce_messages(size)
        consume_time = consume_messages()
        
        produce_throughput = BATCH_SIZE / produce_time
        consume_throughput = BATCH_SIZE / consume_time
        
        print(f"Payload Size: {size} bytes, Produce Throughput: {produce_throughput:.2f} messages/sec, Consume Throughput: {consume_throughput:.2f} messages/sec")

    consumer.close()
    producer.close()
    client.close()

if __name__ == "__main__":
    main()

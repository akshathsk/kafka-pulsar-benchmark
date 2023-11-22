import pulsar
import time
import json
import string
import random

# Initialize Pulsar client and producer
client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic-1')

def generate_random_string(size):
    """Generate a random string of given size."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def produce_message(payload_size):
    # Generate a random message of the given size
    random_message = generate_random_string(payload_size)

    # Create a message payload with the current timestamp
    message_payload = {
        'message': random_message,
        'timestamp': time.time()
    }

    # Convert the message payload to a byte string
    message_bytes = json.dumps(message_payload).encode('utf-8')

    producer.send(message_bytes)

# Handle deserialization errors gracefully
def safe_json_deserializer(m):
    try:
        return json.loads(m.decode('utf-8'))
    except json.JSONDecodeError:
        print("Failed to decode message: ", m)
        return None

# Initialize Pulsar consumer
consumer = client.subscribe('my-topic-1', subscription_name='my-sub')

def consume_messages():
    msg = consumer.receive(timeout_millis=5000)
    if msg:
        payload = safe_json_deserializer(msg.data())
        if payload:
            latency = time.time() - payload['timestamp']
            print(f"Payload Size: {len(payload['message'])} bytes, Latency: {latency:.4f} seconds")
            consumer.acknowledge(msg)
            return  # Consume only one message

def main():
    # List of varying payload sizes to test
    payload_sizes = [10, 100, 1000, 10_000, 100_000]

    for size in payload_sizes:
        produce_message(size)
        consume_messages()

    consumer.close()
    producer.close()
    client.close()

if __name__ == "__main__":
    main()

from kafka import KafkaConsumer, KafkaProducer
import time
import json
import string
import random

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

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

    future = producer.send('first_kafka_topic_10', value=message_bytes)
    result = future.get(timeout=10)  # wait for max 10 seconds

    # producer.send('first_kafka_topic_10', value=message_bytes)
    producer.flush()

# Handle deserialization errors gracefully
def safe_json_deserializer(m):
    try:
        return json.loads(m.decode('utf-8'))
    except json.JSONDecodeError:
        print("Failed to decode message: ", m)
        return None

# Initialize Kafka consumer
consumer = KafkaConsumer('first_kafka_topic_10',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=safe_json_deserializer)

def consume_messages():
    raw_msgs = consumer.poll(timeout_ms=5000)
    for _, messages in raw_msgs.items():
        for message in messages:
            payload = message.value
            if payload:
                latency = time.time() - payload['timestamp']
                print(f"Payload Size: {len(payload['message'])} bytes, Latency: {latency:.4f} seconds")
                return  # Consume only one message

def main():
    # List of varying payload sizes to test
    payload_sizes = [100_000]

    for size in payload_sizes:
        # print(f"Sending message of size: {size} bytes...")
        produce_message(size)
        consume_messages()

    producer.close()

if __name__ == "__main__":
    main()

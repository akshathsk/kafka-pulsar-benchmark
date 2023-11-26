from kafka import KafkaConsumer, KafkaProducer
import time
import json
import string
import random

BATCH_SIZE = 1000  # number of messages to produce and consume in a batch

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def generate_random_string(size):
    """Generate a random string of given size."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def produce_messages(payload_size):
    start_time = time.time()
    for _ in range(BATCH_SIZE):
        random_message = generate_random_string(payload_size)
        message_payload = {
            'message': random_message,
            'timestamp': time.time()
        }
        message_bytes = json.dumps(message_payload).encode('utf-8')
        producer.send('first_kafka_topic_11', value=message_bytes)
    producer.flush()
    end_time = time.time()
    return end_time - start_time

def safe_json_deserializer(m):
    try:
        return json.loads(m.decode('utf-8'))
    except json.JSONDecodeError:
        print("Failed to decode message: ", m)
        return None

consumer = KafkaConsumer('first_kafka_topic_11',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=safe_json_deserializer)

def consume_messages():
    consumed_count = 0
    start_time = time.time()
    while consumed_count < BATCH_SIZE:
        raw_msgs = consumer.poll(timeout_ms=10000)
        for _, messages in raw_msgs.items():
            consumed_count += len(messages)
    end_time = time.time()
    return end_time - start_time

def main():
    payload_sizes = [1000]

    for size in payload_sizes:
        produce_time = produce_messages(size)
        consume_time = consume_messages()
        
        produce_throughput = BATCH_SIZE / produce_time
        consume_throughput = BATCH_SIZE / consume_time
        
        print(f"Payload Size: {size} bytes, Produce Throughput: {produce_throughput:.2f} messages/sec, Consume Throughput: {consume_throughput:.2f} messages/sec")

    producer.close()

if __name__ == "__main__":
    main()

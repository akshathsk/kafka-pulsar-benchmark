from kafka import KafkaProducer

import string
import random
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def generate_random_string(size):
    """Generate a random string of given size."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

random_message = generate_random_string(10)
message_payload = {
            'message': random_message,
            'timestamp': time.time()
        }
message_bytes = json.dumps(message_payload).encode('utf-8')

producer.send('first_kafka_topic', value=message_bytes)

producer.flush()
producer.close()


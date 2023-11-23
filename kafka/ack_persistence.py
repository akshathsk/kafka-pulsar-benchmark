from kafka import KafkaProducer
import time


# nvestigating how Kafka and Pulsar handle acknowledgements and message persistence involves creating Python programs that specifically focus on these aspects. This investigation can be broken down into two parts: one for Kafka and one for Pulsar.

# Kafka Acknowledgements and Persistence
# Kafka's message persistence and acknowledgement behavior can be controlled through producer configurations. The key configurations are acks and linger.ms.

# acks: Controls how many partition replicas must receive the record before the producer can consider the write successful.
# linger.ms: Controls the amount of time to buffer data before sending it to the broker.

def produce_messages(acks, linger_ms):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        acks=acks,
        linger_ms=linger_ms
    )

    start_time = time.time()
    for i in range(100):
        message = f'Message {i}'.encode('utf-8')
        producer.send('first_kafka_topic', value=message)

    producer.flush()
    end_time = time.time()
    producer.close()

    print(f"Acks: {acks}, Linger ms: {linger_ms}, Time taken: {end_time - start_time:.2f} seconds")

# Example usage
produce_messages(acks='all', linger_ms=5)
produce_messages(acks='1', linger_ms=5)
produce_messages(acks='0', linger_ms=5)

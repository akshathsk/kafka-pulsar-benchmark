# Kafka

docker-compose -f docker-compose.yml up -d

python3 throughput.py
python3 latency.py

docker exec -it kafka /bin/sh

docker exec -it kafka bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic first_kafka_topic
kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic first_kafka_topic --partitions 10
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic first_kafka_topic





# Pulsar 

docker run -it -p 6650:6650 -p 8080:8080 --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:3.1.1 bin/pulsar standalone

python3 latency_pulsar.py


docker exec -it trusting_wozniak /bin/bash
bin/pulsar-admin topics create-partitioned-topic persistent://public/default/my-topic-1 --partitions 5
bin/pulsar-admin topics update-partitioned-topic persistent://public/default/my-topic-1 --partitions 10
bin/pulsar-admin topics partitioned-stats persistent://public/default/my-topic-1

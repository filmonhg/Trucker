from kafka import (KafkaClient, KeyedProducer, HashedPartitioner,
                   RoundRobinPartitioner)

kafka = KafkaClient("localhost:9092")

# HashedPartitioner is default
producer = KeyedProducer(kafka)
producer.send_messages("filmon-topic2", "key1", "some message KEYED")
producer.send_messages("filmon-topic2", "key2", "this methode KEYED XXRR")

producer = KeyedProducer(kafka, partitioner=RoundRobinPartitioner)

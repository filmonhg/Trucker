#Author Filmon
#Code to produce data to Kafka
import os
import sys
from kafka import SimpleProducer, KafkaClient,KeyedProducer

source_file='/home/ubuntu/truckBenefitMaximaization/data_generation/test_data.csv'
topic="draft_data"
kafka = KafkaClient("localhost:9092")
#this is to create topic if it doesn't exist
#I still have to work on to check if it already existed !!!
#os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 2 --topic draft_data")
producer = SimpleProducer(kafka)
with open(source_file) as f:
	for line in f:
		producer.send_messages(topic,line.rstrip())
f.close()
print "Kafka Produced data to topic \"%s\"" %topic


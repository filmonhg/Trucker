#Author Filmon
#Code to produce data to Kafka
#This is if you want to push historical data to HDFS via Kafka(no need though)

import os
import sys
from kafka import SimpleProducer, KafkaClient,KeyedProducer

source_file='/home/ubuntu/Trucker/file_generator_code/test_data_simple.csv'
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


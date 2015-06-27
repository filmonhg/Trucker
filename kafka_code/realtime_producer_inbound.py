import os
import sys
import time
from kafka import SimpleProducer, KafkaClient,KeyedProducer
source_file='/home/ubuntu/Trucker/data_generation/test_data_simple.csv'
kafka = KafkaClient("localhost:9092")
#this is to create topic if it doesn't exist
#I still have to work on to check if it already existed !!!
#os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 2 --topic real_time_data_inbound")
producer = SimpleProducer(kafka)
while True:
	with open(source_file) as f:
		for line in f:
			producer.send_messages("real_time_data_inbound",line.rstrip())
			time.sleep(0.5)
		f.close()
#def ProduceData(Topic):
	# To send messages synchronously
	# Note that the application is responsible for encoding messages to type str
#producer.send_messages("filmon_test_topic3", "some message creating topic")
#



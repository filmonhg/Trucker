#Author Filmon 
#Real time inbound data producer sending it to spout of Storm
import os
import sys
import time
from kafka import SimpleProducer, KafkaClient,KeyedProducer
source_file='/home/ubuntu/Trucker/data_generation/inbound_today.csv'
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



import os
import sys
from kafka import SimpleProducer, KafkaClient,KeyedProducer
source_file='/home/ubuntu/truckBenefitMaximaization/data_generation/test_data.csv'
kafka = KafkaClient("localhost:9092")
#this is to create topic if it doesn't exist
#I still have to work on to check if it already existed !!!
os.system("/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 2 --topic sample_outbounds")
producer = SimpleProducer(kafka)
with open(source_file) as f:
	for line in f:
		producer.send_messages("sample_outbounds",line.rstrip())
f.close()
#def ProduceData(Topic):
	# To send messages synchronously
	# Note that the application is responsible for encoding messages to type str
#producer.send_messages("filmon_test_topic3", "some message creating topic")
#



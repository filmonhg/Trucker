#Author Filmon 
#Consumer kafka code
import os
import sys
from kafka import KafkaClient, SimpleConsumer

#kafka=KafkaClient("ec2-52-8-194-192.us-west-1.compute.amazonaws.com:9092")
kafka=KafkaClient("ec2-52-8-194-192.us-west-1.compute.amazonaws.com")

kafka_consumer=SimpleConsumer(kafka,"my_group","outbound_sample_topic")

messages= kafka_consumer.get_messages(count=1000, block=False)
if not messages:
            print "no messages to read"
for message in messages:
	print  message.message.value

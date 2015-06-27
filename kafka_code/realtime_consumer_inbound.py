#Author Filmon 
#Consumer kafka code
import os
import sys
from kafka import KafkaClient, SimpleConsumer

domain="ec2-52-8-124-34.us-west-1.compute.amazonaws.com"
group="my_group"
#topic="outbound_sample_topic"
#topic="thomas_topic"
#topic="test_data_topics3"
topic="real_time_data_inbound"
#kafka=KafkaClient("ec2-52-8-194-192.us-west-1.compute.amazonaws.com:9092")
kafka=KafkaClient(domain)
tmp_file_path="/tmp/kafka_%s_%s.csv" % (topic, group)
def consume_save(group,topic):
#	tmp_save=open(tmp_file_path,"w")
	while True:
		kafka_consumer=SimpleConsumer(kafka,group,topic)
		messages= kafka_consumer.get_messages(count=1000, block=False)
		if not messages:
			print "Consumer didn't read any messages"
		for message in messages:
	#		tmp_save.write( message.message.value+"\n")
			print message.message.value+"\n"
			kafka_consumer.commit() # inform zookeeper of position in the kafka queu
#/hadoop_dir_outbound_sample_topic/hadoop_dirsample_file.csv
def push_to_hdfs(tmp_file_path):
	hadoop_dir="hadoop_dir_%s_%s" %(group,topic)
	hdfs_file_name="hdfs_file.txt"
#	os.system("hdfs dfs -rmdir /%s_%s" % (hadoop_dir,topic))
	os.system("hdfs dfs -mkdir /%s" % hadoop_dir)
	print "pushing to file \n"
	#os.system("touch %s" % hadoop_file_path)
	os.system("hdfs dfs -copyFromLocal %s /%s/%s" % (tmp_file_path,hadoop_dir,hdfs_file_name))

consume_save(group,topic)
#print "pushed to temp file \n"
#push_to_hdfs(tmp_file_path)

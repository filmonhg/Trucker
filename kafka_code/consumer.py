#Author Filmon 
#Consumer kafka code
#Consumes data saves it in temporary file and pushes it  to hdfs
import os
import sys
from kafka import KafkaClient, SimpleConsumer

domain="ec2-52-8-194-192.us-west-1.compute.amazonaws.com"
group="my_group"
topic="draft_data"
kafka=KafkaClient(domain)
tmp_file_path="/tmp/kafka_%s_%s.csv" % (topic, group)

#method to consume and save it to temporary file
def consume_save(group,topic):
	tmp_save=open(tmp_file_path,"w")
	kafka_consumer=SimpleConsumer(kafka,group,topic)
	messages= kafka_consumer.get_messages(count=1000, block=False)
	if not messages:
		print "Consumer didn't read any messages"
	for message in messages:
		tmp_save.write( message.message.value+"\n")
#		print message.message.value+"\n"
	print ".... ... .. .."
	print "Message from topic \"%s\" consumed \n" % topic
#push the temporary fiele to hdfs
def push_to_hdfs(tmp_file_path):
	hadoop_dir="hadoop_dir_%s_%s" %(group,topic)
	hdfs_file_name="hdfs_file.txt"
#	os.system("hdfs dfs -rmdir /%s_%s" % (hadoop_dir,topic))
#	os.system("hdfs dfs -mkdir /%s" % hadoop_dir)
	print "pushing to file \n"
	print ".... ... .. .."
	#os.system("touch %s" % hadoop_file_path)
	#os.system("hdfs dfs -copyFromLocal %s /%s/%s" % (tmp_file_path,hadoop_dir,hdfs_file_name))
	os.system("hdfs dfs -put -f %s /%s/%s" % (tmp_file_path,hadoop_dir,hdfs_file_name))
	print "pushed to file \n"
consume_save(group,topic)
push_to_hdfs(tmp_file_path)

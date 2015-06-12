#Author: Filmon
#Shell script to push data to hdfs with Kafka
#!/bin/bash  
python producer.py 
python consumer.py 
hdfs dfs -ls /hadoop_dir_my_group_draft_data
hdfs dfs -cat /hadoop_dir_my_group_draft_data/hdfs_file.txt

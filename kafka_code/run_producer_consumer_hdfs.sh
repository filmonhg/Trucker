#Author: Filmon
#Shell script to push data to hdfs with Kafka
#!/bin/bash  
echo "Producer running ..."
python producer.py 
echo "Producer finished .. "
echo "Consumer running ..."
python consumer.py 
echo "Producer finished .. "
echo "Listing files that are stored in to HDFS "
hdfs dfs -ls /hadoop_dir_my_group_draft_data
echo "display contents of the HDFS stored file "
hdfs dfs -cat /hadoop_dir_my_group_draft_data/hdfs_file.csv

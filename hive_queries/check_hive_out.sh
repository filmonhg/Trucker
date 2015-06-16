#Author Filmon
#script to display the output of hive output
#!/bin/bash

hdfs dfs -cat /hadoop_dir_my_group_draft_data_hive_output/draft_output_hive/000000_0
#hdfs dfs -cat /hadoop_dir_my_group_draft_data_hive_output/outbound_output_hive/000000_0

getting output
-------------
*ByState: is for state wise queries using hive from hdfs and scipts to push to Cassandra
*ByCity: is for city, state queries using hive from hdfs and scripts to push to Cassandra
* Read me on how to use the hive output
* This will display trucks departing from Florida
hdfs dfs -cat /hadoop_dir_my_group_draft_data/draft_output_hive/000000_0

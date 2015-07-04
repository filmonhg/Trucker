#Author Filmon 
#shell script to transfer data from hive to cassandra (for testing purposes only)
#!/bin/bash
hive -f outbound_test1.sql >test_hive_output
cat test_hive_output | python aggregate.py

#Author: Filmon
#Script to create table in hive and push it to Cassandra (inbound state)
#!/bin/bash
hive -f inbound_hive_state_yr.sql >tmp_inbound_state
cat tmp_inbound_state | python inbound_state_yr_cassandra.py

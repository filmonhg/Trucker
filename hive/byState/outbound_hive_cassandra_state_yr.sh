#Author: Filmon
#Script to create table in hive and push it to Cassandra (outbound state)
#!/bin/bash
hive -f outbound_hive_state_yr.sql >tmp_outbound_state
cat tmp_outbound_state | python outbound_state_yr_cassandra.py

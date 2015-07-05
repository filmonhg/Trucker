#Author: Filmon
#script to create inbound city-state table in hive and push to Cassandra
#!/bin/bash
hive -f inbound_hive_city_yr.sql >tmp_inbound_city_state
cat tmp_inbound_city_state | python inbound_city_yr_cassandra.py

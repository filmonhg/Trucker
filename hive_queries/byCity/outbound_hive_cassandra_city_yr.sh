#Author: Filmon
#Script to create outbound city-state table in hive and push to cassandra
#!/bin/bash
hive -f outbound_hive_city_yr.sql >tmp_outbound_city_state
cat tmp_outbound_city_state | python outbound_city_yr_cassandra.py

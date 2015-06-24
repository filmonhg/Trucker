#!/bin/bash
hive -f inbound_hive_state_yr.sql >tmp_inbound_state
cat tmp_inbound_state | python inbound_state_yr_cassandra.py

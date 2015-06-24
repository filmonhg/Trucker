#!/bin/bash
hive -f outbound_hive_state_yr.sql >tmp_outbound_state
cat tmp_outbound_state | python outbound_state_yr_cassandra.py

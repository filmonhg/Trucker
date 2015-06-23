#!/bin/bash
hive -f outbound_test1.sql >test_hive_output
cat test_hive_output | python aggregate.py

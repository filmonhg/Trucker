#Author: Filmon
#!/usr/bin/python
#This will push the outbound state table to cassandra

#import libraries
import os, sys
from cqlengine import columns
from cqlengine.models import Model
from cqlengine import connection
from cqlengine.management import sync_table

# Define a model
class outbound_state(Model):
	c_state = columns.Text(primary_key=True)
	c_count = columns.Text()
	c_year = columns.Text(primary_key=True,clustering_order="DESC")
	def __repr__(self):
		return '%s %s %s' % (self.c_state,self.c_year,self.c_count)
connection.setup(['127.0.0.1'], "outbound_cassandra")
sync_table(outbound_state)
for line in sys.stdin:
	f = line.split('\t')
	outbound_state.create(c_year=str(f[0].strip()),c_state=str(f[1].strip()),c_count=str(f[2].strip()))


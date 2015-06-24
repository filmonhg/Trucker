#!/usr/bin/python
#This will push the table to cassandra

#import os, cql, sys
import os, sys
#from time import strftime
#from datetime import datetime
from cqlengine import columns
from cqlengine.models import Model
from cqlengine import connection
from cqlengine.management import sync_table

# Define a model
class inbound_state(Model):
	c_state = columns.Text(primary_key=True)
	c_count = columns.Text()
	c_year = columns.Text(primary_key=True,clustering_order="DESC")
	def __repr__(self):
		return '%s %s %s' % (self.c_year,self.c_state,self.c_count)
connection.setup(['127.0.0.1'], "outbound_cassandra")
sync_table(inbound_state)
#inbound_state.create(c_city='Franklin', c_state='TN', c_count='5', c_year='2015')
for line in sys.stdin:
	f = line.split('\t')
	inbound_state.create(c_state=str(f[1].strip()), c_count=str(f[2].strip()), c_year=str(f[0].strip()))
#p=inbound_state.get(c_city='Manchester')
#print p
#q=inbound_state.objects()
#for i in q:
#	print i


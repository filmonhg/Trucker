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
class inbound_city_state(Model):
	c_city  = columns.Text(primary_key=True)
	c_state = columns.Text(primary_key=True)
	c_count = columns.Text()
	c_year = columns.Text(primary_key=True,clustering_order="DESC")
	def __repr__(self):
		return '%s %s %s %s' % (self.c_year,self.c_city,self.c_state,self.c_count)
# Define a model
class inbound_city_state_major(Model):
        c_year  = columns.Text(primary_key=True)
        c_city = columns.Text(primary_key=True)
        c_state = columns.Text(primary_key=True,clustering_order="DESC")
        c_count = columns.Text()
        def __repr__(self):
                return '%s %s %s %s' % (self.c_year,self.c_city,self.c_state,self.c_count)



connection.setup(['127.0.0.1'], "outbound_cassandra")
sync_table(inbound_city_state)
sync_table(inbound_city_state_major)
#inbound_city_state.create(c_city='Franklin', c_state='TN', c_count='5', c_year='2015')
for line in sys.stdin:
	f = line.split('\t')
	inbound_city_state.create(c_state=str(f[2].strip()), c_count=str(f[3].strip()), c_year=str(f[0].strip()),c_city=str(f[1].strip()))
#p=inbound_city_state.get(c_city='Manchester')
#print p

major_cities = { 
'Wichita':'KS',
'Memphis':'TN',
'Sacramento':'CA',
'Seattle':'WA',
'San Diego':'CA',
'Chicago':'IL',
'Memphis':'TN',
'Austin':'TX',
'Los Angeles':'CA',
'Chicago':'IL',
'Boston':'MA',
'Kansas City':'MO',
'New York':'NY',
'Memphis':'TN',
'Los Angeles':'CA',
'Memphis':'TN',
'Omaha':'NE',
'Portland':'OR',
'Atlanta':'GA',
'Jacksonville':'FL',
'Fort Worth':'TX',
'Mesa':'AZ',
'Oakland':'CA',
'San Antonio':'TX',
'Memphis':'TN',
'Atlanta':'GA',
'Los Angeles':'CA',
'Indianapolis':'IN',
'Fresno':'CA',
'Houston':'TX',
'Washington':'DC',
'Houston':'TX',
'Los Angeles':'CA',
'Atlanta':'GA',
'Nashville':'TN',
'Denver':'CO',
'Charlotte':'NC',
'Baltimore':'MD',
'El Paso':'TX',
'San Jose':'CA',
'Las Vegas':'NV',
'Phoenix':'AZ',
'Chicago':'IL',
'New Orleans':'LA',
'Chicago':'IL',
'Memphis':'TN',
'Long Beach':'CA',
'Louisville':'KY',
'Atlanta':'GA',
'Houston':'TX',
'Minneapolis':'MN',
'Tulsa':'OK',
'Cleveland':'OH',
'Houston':'TX',
'Atlanta':'GA',
'Oklahoma City':'OK',
'Philadelphia':'PA',
'Los Angeles':'CA',
'Raleigh':'NC',
'Chicago':'IL',
'Houston':'TX',
'Arlington':'TX',
'Chicago':'IL',
'Tucson':'AZ',
'Detroit':'MI',
'Houston':'TX',
'Dallas':'TX',
'Columbus':'OH',
'Milwaukee':'WI',
'Los Angeles':'CA',
'Atlanta':'GA',
'Miami':'FL',
'Albuquerque':'NM',
'San Francisco':'CA',
}
for key in major_cities:
	q=inbound_city_state.objects(c_city=key,c_state=major_cities[key])
	for i in q:
		inbound_city_state_major.create(c_year=i.c_year,c_city=i.c_city,c_state=i.c_state,c_count=i.c_count)

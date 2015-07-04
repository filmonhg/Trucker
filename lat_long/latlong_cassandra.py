#Author: Filmon
#Script for pushing lat long table directly to Cassandra
#This is to make it easy for front end to map each city in the map
#!/usr/bin/python
from cqlengine import columns
from cqlengine.models import Model
from cqlengine import connection
from cqlengine.management import sync_table


# Define a model
class city_state_lat_lng(Model):
        c_city  = columns.Text(primary_key=True)
        c_state = columns.Text(primary_key=True)
        c_lat = columns.Text()
        c_lng = columns.Text()
        def __repr__(self):
                return '%s %s %s %s %s' % (self.city,self.c_state,self.c_lat,self.c_lng)

connection.setup(['127.0.0.1'], "outbound_cassandra")
sync_table(city_state_lat_lng)
    
lines=open("cities.csv",'r')
for line in lines:
	f=line.split(',')

	city=str(f[2].strip())
	state=str(f[1].strip())
	lat=str(f[3].strip())
	lng=str(f[4].strip())
	print city+" "+state+" "+lat+" "+lng	
	city_state_lat_lng.create(c_city=city, c_state=state, c_lat=lat, c_lng=lng)


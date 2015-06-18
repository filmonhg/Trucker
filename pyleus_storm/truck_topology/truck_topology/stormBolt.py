#!/usr/bin/python
# This program creates a storm bolt that filters the incoming tuples based on occupancy
# It stores the unoccupied cab details into HBase which are then shown on UI. The HBase
# table is refreshed every 5 seconds using a tick tuple.
import logging
from pyleus.storm import SimpleBolt
from cqlengine import columns
from cqlengine.models import Model
from cqlengine import connection
from cqlengine.management import sync_table


log = logging.getLogger("truckLogger")
counter_dict = {}

# Define a model
class outbound_real_count(Model):
        c_city  = columns.Text(primary_key=True)
        c_state = columns.Text(primary_key=True)
        #c_count = columns.Counter()
        c_count = columns.Integer()
        c_year = columns.Text(primary_key=True,clustering_order="DESC")
        def __repr__(self):
                return '%s %s %s %s' % (self.c_year,self.c_city,self.c_state,self.c_count)

connection.setup(['127.0.0.1'], "outbound_cassandra")
sync_table(outbound_real_count)

class firstBolt(SimpleBolt):
    OUTPUT_FIELDS = ['trucks']
    
#    def initialize(self):
#        self.unoccCabs = {}        

    def process_tuple(self, tup):
        result, = tup.values
	f = result.split(',')
        log.debug("+++++++++++result++++++++++++++++")
        log.debug(result)
        log.debug("+++++++++++fffff++++++++++++++++")
        log.debug(f)
	city=str(f[7].strip())
	state=str(f[8].strip())
	year=str(f[3].strip())
	count=str(f[9].strip())
        log.debug(city)
        log.debug(state)
        log.debug(year)
        log.debug(count)
	city_state=city+state
	log.debug(city_state)
	if city_state not in counter_dict:
		counter_dict[city_state] =1
	else:
		counter_dict[city_state] +=1
	log.debug(counter_dict[city_state])
		
	
	outbound_real_count.create(c_city=city, c_state=state, c_count=counter_dict[city_state], c_year=year)
#	outbound_real_count.create(c_city=city, c_state=state, str(c_count), c_year=year)
if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG,filename='/tmp/truck_topology.log',format="%(message)s",filemode='a')
	firstBolt().run()


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

# Define a model
class outbound_real_count(Model):
        c_city  = columns.Text(primary_key=True)
        c_state = columns.Text(primary_key=True)
        c_count = columns.Text()
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
	c_city=str(f[7].strip())
	c_state=str(f[8].strip())
	c_year=str(f[3].strip())
	c_count=str(f[9].strip())
        log.debug(c_city)
        log.debug(c_state)
        log.debug(c_year)
        log.debug(c_count)
	outbound_real_count.create(c_city=str(f[7].strip()), c_state=str(f[8].strip()), c_year=str(f[3].strip()),c_count=str(f[9].strip()))

#outbound_real_count.create(c_city='Oakland', c_state='CA', c_count='10', c_year='2016')
if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG,filename='/tmp/truck_topology.log',format="%(message)s",filemode='a')
	firstBolt().run()


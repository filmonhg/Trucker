#!/usr/bin/python
# This program creates a storm bolt that filters the incoming tuples based on occupancy
# It stores the unoccupied cab details into HBase which are then shown on UI. The HBase
# table is refreshed every 5 seconds using a tick tuple.
import logging
from pyleus.storm import SimpleBolt
#from cqlengine import columns
#from cqlengine.models import Model
#from cqlengine import connection
#from cqlengine.management import sync_table


log = logging.getLogger("truckLogger")

class firstBolt(SimpleBolt):
    OUTPUT_FIELDS = ['trucks']
    
#    def initialize(self):
#        self.unoccCabs = {}        

    def process_tuple(self, tup):
        result, = tup.values
        log.debug("+++++++++++result++++++++++++++++")
        log.debug(result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,filename='/tmp/truck_topology.log',format="%(message)s",filemode='a')
    firstBolt().run()


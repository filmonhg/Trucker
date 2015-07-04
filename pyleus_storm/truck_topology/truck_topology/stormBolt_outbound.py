#Author: Filmon
#!/usr/bin/python
# This program is the bolt where the real time count of cities is executed
#THe counts are updated to cassandra in real time 
# table is refreshed every 5 seconds using a tick tuple as set in the topology

#importing libraries
import logging
from pyleus.storm import SimpleBolt
from cqlengine import columns
from cqlengine.models import Model
from cqlengine import connection
from cqlengine.management import sync_table


log = logging.getLogger("truckLogger") #log for debugging purposesi
counter_dict = {}
counter_dict_state = {}

# Define a model (table by city,state))
class outbound_real_count(Model):
        c_city  = columns.Text(primary_key=True)
        c_state = columns.Text(primary_key=True)
        #c_count = columns.Counter()
        c_month_day = columns.Text(primary_key=True,clustering_order="DESC")
        c_count = columns.Integer()
        def __repr__(self):
                return '%s %s %s %s' % (self.c_city,self.c_state,self.c_month_day,self.c_count)

# Define a model (table by state)
class outbound_real_count_state(Model):
        c_state = columns.Text(primary_key=True)
        c_month_day = columns.Text(primary_key=True,clustering_order="DESC")
        c_count = columns.Integer()
        def __repr__(self):
                return '%s %s %s' % (self.c_state,self.c_month_day,self.c_count)

connection.setup(['127.0.0.1'], "outbound_cassandra")
sync_table(outbound_real_count)
sync_table(outbound_real_count_state)

class firstBolt(SimpleBolt):
    OUTPUT_FIELDS = ['trucks']
    
    def process_tuple(self, tup):
        result, = tup.values
	f = result.split(',')
#        log.debug("+++++++++++result++++++++++++++++")
#        log.debug(result)
#        log.debug("+++++++++++fffff++++++++++++++++")
#        log.debug(f)
	city=str(f[7].strip())
	state=str(f[8].strip())
	day=str(f[2].strip())
	month=str(f[1].strip())
#        log.debug(city)
#        log.debug(state)
	city_state=city+state
	month_day=month+day
#        log.debug(month_day)
#	log.debug(city_state)
	if city_state not in counter_dict:
		counter_dict[city_state] =1
	else:
		counter_dict[city_state] +=1
	log.debug(counter_dict[city_state])
		

	if state not in counter_dict_state:
		counter_dict_state[state] =1
	else:
		counter_dict_state[state] +=1
	
	outbound_real_count.create(c_city=city, c_state=state,c_month_day=month_day, c_count=counter_dict[city_state])
	outbound_real_count_state.create(c_state=state,c_month_day=month_day, c_count=counter_dict_state[state])

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG,filename='/tmp/truck_topology.log',format="%(message)s",filemode='a')
	firstBolt().run()


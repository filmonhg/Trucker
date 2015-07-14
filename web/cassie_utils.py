#Author: Filmon
#Class for querying from Cassandra
from cassandra.cluster import Cluster
from datetime import datetime, timedelta

class CassieUtilities(object):

    def __init__(self, ip_addr='52.8.124.34', keyspace='outbound_cassandra'):
        cluster = Cluster([ip_addr])
        self.session = cluster.connect()
        self.session.set_keyspace(keyspace)

    def fetch_daterange_state(self, table):
        record_lookup_stmt = "SELECT * FROM {}".format(table)
  	record_list=[]
        record_list = self.session.execute(record_lookup_stmt)
        return record_list

    def fetch_daterange(self, table,city,state):
        record_lookup_stmt = "SELECT * FROM {} WHERE c_city=%s AND c_state=%s".format(table)
  	record_list=[]
        record_list = self.session.execute(record_lookup_stmt, [city,
								state])
        return record_list

    def fetch_major_by_year(self, table,year):
        record_lookup_stmt = "SELECT * FROM {} WHERE c_year=%s".format(table)
  	record_list=[]
        record_list = self.session.execute(record_lookup_stmt, [year])
        return record_list
         

    def fetch_state_by_year(self, table,year):
        record_lookup_stmt = "SELECT * FROM {} WHERE c_year=%s".format(table)
  	record_list=[]
        record_list = self.session.execute(record_lookup_stmt, [year])
        return record_list


    def fetch_state_realtime(self, table):
        record_lookup_stmt = "SELECT * FROM {}".format(table)
  	record_list=[]
        record_list = self.session.execute(record_lookup_stmt)
        return record_list

    def fetch_lat_lng(self, table,city,state):
        record_lookup_stmt = "SELECT * FROM {} WHERE c_city=%s AND c_state=%s".format(table)
  	record_list=[]
        record_list = self.session.execute(record_lookup_stmt, [city,state])
        return record_list

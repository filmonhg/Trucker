--Author: Filmon
--For creating table by State for outbound from HDFS using Hive prior to pushing it to Cassandra
DROP TABLE IF EXISTS outbound_data_state;

CREATE EXTERNAL TABLE  outbound_data_state (time string, day string,month string,year string,truck_type string,f_p string,dh_o string,origin_city string,origin_state string, trip string,destination_city string, destination_state string,dh_d string, contact string, credit string, dtp string, ft string, klbs string, company string, tia string, dc string, factor string, mkt_rates string, assure string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "\054" LINES TERMINATED BY "\n"
STORED AS TEXTFILE LOCATION '/hadoop_OUTBOUND/';


SELECT year,origin_state,count(1)
FROM outbound_data_state
GROUP BY year,origin_state
--WHERE origin_state='FL'


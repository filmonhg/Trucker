
DROP TABLE IF EXISTS outbound_data;

CREATE EXTERNAL TABLE  outbound_data (time string, day string,month string,year string,truck_type string,f_p string,dh_o string,origin_city string,origin_state string, trip string,destination_city string, destination_state string,dh_d string, contact string, credit string, dtp string, ft string, klbs string, company string, tia string, dc string, factor string, mkt_rates string, assure string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "\054" LINES TERMINATED BY "\n"
STORED AS TEXTFILE LOCATION '/hadoop_OUTBOUND/';

--DESCRIBE draft_data;

SELECT year,origin_city,origin_state,count(1)
FROM outbound_data
GROUP BY year,origin_city,origin_state
--WHERE origin_state='FL'


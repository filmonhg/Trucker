
DROP TABLE IF EXISTS draft_data;

CREATE EXTERNAL TABLE  draft_data (time string, day string,month string,year string,truck_type string,f_p string,dh_o string,origin_city string,origin_state string, trip string,destination_city string, destination_state string,dh_d string, contact string, credit string, dtp string, ft string, klbs string, company string, tia string, dc string, factor string, mkt_rates string, assure string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "\054" LINES TERMINATED BY "\n"
STORED AS TEXTFILE LOCATION '/hadoop_dir_my_group_draft_data/';
--STORED AS TEXTFILE LOCATION '/hadoop_dir_my_group_draft_data';

--DESCRIBE target;

--INSERT OVERWRITE DIRECTORY '/hadoop_dir_my_group_draft_data_hive_output/outbound_output_hive'
--ROW FORMAT DELIMITED FIELDS TERMINATED BY "\t" LINES TERMINATED BY "\n"
--SELECT time,day,month,year,origin_city,origin_state,trip, destination_city,destination_state
--SELECT time
--FROM target

--DESCRIBE draft_data;

--set year=SPLIT(day,'/')
--INSERT OVERWRITE DIRECTORY '/hadoop_dir_my_group_draft_data_hive_output/draft_output_hive'
--ROW FORMAT DELIMITED FIELDS TERMINATED BY "\t" LINES TERMINATED BY "\n"
--SELECT origin_city,trip,destination_city
--FROM draft_data
--SELECT origin_city, origin_state, trip, destination_city, destination_state
SELECT year,origin_city,origin_state,count(1)
FROM draft_data
GROUP BY year,origin_city,origin_state
--WHERE origin_state='FL'


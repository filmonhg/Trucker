DROP TABLE IF EXISTS staging_table;

CREATE EXTERNAL TABLE  staging_table (raw_data string)
ROW FORMAT DELIMITED LINES TERMINATED BY "\n"
STORED AS TEXTFILE LOCATION '/hadoop_dir_my_group_draft_data/';

DROP TABLE IF EXISTS draft_data;

CREATE EXTERNAL TABLE  draft_data (time string, day string,month string,year string,truck_type string,f_p string,dh_o string,origin_city string,origin_state string, trip string,destination_city string, destination_state string,dh_d string, contact string, credit string, dtp string, ft string, klbs string, company string, tia string, dc string, factor string, mkt_rates string, assure string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "\054" LINES TERMINATED BY "\n"
STORED AS TEXTFILE LOCATION '/hadoop_dir_my_group_draft_data/';
--STORED AS TEXTFILE LOCATION '/hadoop_dir_my_group_draft_data';

DROP TABLE IF EXISTS target;
CREATE TABLE target AS SELECT
rw[0] AS time,rw[1] AS day,rw[2] AS month,rw[3] AS year,
rw[4] AS truck_type,rw[5] AS f_p,rw[6] AS dh_o, rw[7] AS origin_city,
rw[8] AS origin_state, rw[9] AS trip,rw[10] AS destination_city,
rw[11] AS destination_state, rw[12] AS dh_d, rw[13] AS contact,
rw[14] AS credit, rw[15] AS dtp,rw[16] AS ft, rw[17] AS klbs,
rw[18] AS company, rw[19] AS tia,rw[20] AS dc, rw[21] AS factor,
rw[22] AS mkt_rates, rw[23] AS assure
FROM (SELECT split(raw_data,",/") AS rw from staging_table) t;  

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


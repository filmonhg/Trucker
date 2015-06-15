DROP TABLE draft_data;

CREATE EXTERNAL TABLE IF NOT EXISTS draft_data (time string, day string,truck_type string,f_p string,dh_o string,origin_city string,origin_state string, trip string,destination_city string, destination_state string,dh_d string, contact string, credit string, dtp string, ft string, klbs string, company string, tia string, dc string, factor string, mkt_rates string, assure string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "\054" LINES TERMINATED BY "\n"
STORED AS TEXTFILE LOCATION '/hadoop_dir_my_group_draft_data/';
--STORED AS TEXTFILE LOCATION '/hadoop_dir_my_group_draft_data';

DESCRIBE draft_data;

--set year=SPLIT(day,'/')
INSERT OVERWRITE DIRECTORY '/hadoop_dir_my_group_draft_data_hive_output/draft_output_hive'
ROW FORMAT DELIMITED FIELDS TERMINATED BY "\t" LINES TERMINATED BY "\n"
--SELECT origin_city, origin_state, trip, destination_city, destination_state
SELECT origin_state,destination_state,count(1)
FROM draft_data
GROUP BY origin_state,destination_state
--WHERE origin_state='FL'


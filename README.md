# Trucker
=============
*Documentation is work in progress ...*
Truck Transport Benefit Tracker
-------------------------------
[www.truckers.solutions] (http://www.truckers.solutions/)

Table of Contents:
-------------------
1. [Introduction] (README.md#1- Introduction)
2. [How it Works] (README.md#2- How it works)
3. [Architecture] (README.md#3- Architecture)
4. [API] (README.md#4- API)

## 1. Introduction
Trucker is a tool for tracking track transport system all over US cities to allow carriers or brokers make informed decisions that maximize their benefit by looking at available load versus number of trucks in each city. The tool provides both real-time and historical updates of trucks/load using the following tools:
- Apache Kafka
- Apache HDFS
- Hive
- Apache Storm
- Apache Cassandra
- Flask with simplemap, HighCharts, Bootstrap and Ajax

## 2. How it Works
Trucker uses two sources of engineered data namely inbound data(for trucks/load coming to a city)  and outbound data(for trucks/load going to a city) for both historical and real time data. For historical, it ingests ~200GB of data for years 2004 to 2014. Real time data is processed in real time to reflect the status directly to user while at the same time pushing the data in micro-batches to the batch layer.

[Trucker Demo] (https://www.youtube.com/watch?v=T2laLdZ9gTg&spfreload=10)

## 3. Architecture
![Architecture] (img/architecture.png)

#Data Generation
Two sources of data (Inbound and Outbound) was generated that looks like the follwing.
![Inbound data] (img/inbound_data.png)
![Outbound data] (img/outbound_data.png)
* Time stamp is randomized over period of 10 years (2004 - 2014)
* Random choice of cities was made for source and destination, where the randomization was biased to the major cities (for cities with population of 6000+,[http://www.city-data.com/] (http://www.city-data.com/)). Source of all cities obtained from [All_cities](http://www.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv ) that has 42742 cities.
* To get mile (distance) between cities, latitude and longitude of each city was used to approximate the distance using Vincenty distance method which gives fairly similar distance provided by google API. This is mainly due to limitation of google API calls that limit you to generate huge amount of data in short time.
* Running multiple random data generation script easily allow you to generate huge inbound and outbound data in short time.

#Data Ingestion
csv messages were produced and consumed by python scrpts using kafka-python package from https://github.com/mumrah/kafka-python.git. messages were published to two topics (inbound and outbound) with Storm streaming and HDFS acting as consumers. Messages were blockd into 20MB size micro batches and then pushing it to HDFS making it available for the batch layer when performing complete recomputation.
#Batch Processing
Batch processing performs count of inbound and outbound trucks for each city and state using  historical data from 2004 - 2014. Aggregate views for serving queries at the user end are generated with Hive. The aggregated data was then directly written to cassandra using Python client library for Apache Cassandra.
#Real-Time Processing
There are two topologies (for inbound and outbound) for processing real-time data each comprising of a kafka-spout and a bolt (with tick interval frequency of 5 sec). The spout takes data from Kafka in real time and the bolt takes from spout and process it prior to writing it to Cassandra. Pyleus-storm driver from (https://github.com/Yelp/pyleus) was used on top of Apache storm to allow python implementation.
#Cassandra Schema
Primary key and partition key are chosen in such a way that maximizes the efficient acccess of tuple from Cassandra

Batch Tables

1. outbound_city_state c_city (PK), (c_state,c_year(Partition key)), c_count
2. outbound_city_state_major c_city (PK), (c_state,c_year(Partition key)),c_count
3. inbound_city_state c_city (PK), (c_state,c_year(Partition key)), c_count
4. inbound_city_state_major c_city (PK), (c_state,c_year(Partition key)), c_count
5. inbound_state c_year (PK), (c_state(Partition key)), c_count
6. outbound_state c_year (PK), (c_state(Partition key)), c_count

Real Time Tables

1. outbound_real_count c_city(PK),c_state,c__month_day_year (Partition key), c_count
2. inbound_real_count c_city(PK),c_state,c__month_day_year (Partition key), c_count
3. inbound_real_count_state c_city(PK),c_state,c__month_day_year (Partition key), c_count
4. outbound_real_count_state c_state(PK), c_month_day_year (Partition key), c_count


## 4. Startup Protocol
1. Kafka Server
2. Storm Streaming (Submit topologies to name node)
3. HDFS kafka consumer 
4. Kafka message producer

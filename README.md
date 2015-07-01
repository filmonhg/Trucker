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
- Storm
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
* Random choice of cities was made for source and destination, where the randomization was biased to the major cities (for cities with population of 6000+,![http://www.city-data.com/] (http://www.city-data.com/)). Source of all cities obtained from [!All_cities](http://www.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv ) that has 42742 cities.
* To get mile (distance) between cities, longitude and latitude of each city was used to approximate the distance using Vincenty distance method which gives fairly similar distance provided by google API. This is mainly due to limitation of google API calls not being able to generate huge amount of data in short time.
* then run python code from shell script to generate the fake data as big as you want them

#Data Ingestion

#Batch Processing

#Real-Time Processing

#Cassandra Schema
## 4. API

# Trucker
----------
*Documentation is work in progress ...*

Table of Contents:
1. [Introduction] (README.md#1- introduction)

## 1. Introduction
Trucker is a tool for tracking track transport system all over US cities to allow carriers or brokers make informed decisions that maximize their benefit by looking at available load versus number of trucks in each city. The tool provides both real-time and historical updates of trucks/load using the following tools:
- Apache Kafka
- Apache HDFS
- Hive
- Storm
- Flask with simplemap, HighCharts, Bootstrap and Ajax

## 2. How it Works
Trucker uses two sources of data namely inbound data(For trucks/load coming to a city)  and outbound data(for trucks/load going to a city) for both histrical and real time data. For historical, it uses ~200GB of data for years from 2004 to 2014. Real time data is processed in real time to reflect the status directly to user while at the same time pushing the data in micro-batches to the batch layer.

[Trucker Demo] (https://www.youtube.com/watch?v=T2laLdZ9gTg&spfreload=10)


## 4. DATA SOURCE


## 3. Architecture


## 5. API

#!/bin/python

#Program to change file's date to today's
import time

f=open('outbound10.csv','r')

today=(time.strftime("%m,%d,%Y"))	
tmp=today.split(',')
today_month=tmp[0]
today_day=tmp[1]
today_year=tmp[2]
time=time.strftime("%I:%M %p")
#print time
#print today
#print today_month
#print today_day
#print today_year

for line in f:
	row=line.split(',')

	print time+","+today_month+","+today_day+","+today_year+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+row[14]+","+row[15]+","+row[16]+","+row[17]+","+row[18]+","+row[19]+","+row[20]+","+row[21]+","+row[22]+","+row[23].strip()

f.close()

#Author: Filmon
#Script for randomly generating (sythesized data)
import random
import time

#this is for finding distance between two locations using
#their respective longitutde and latitude
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

#for time generation
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)
    #return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

def randomTime(start, end, prop):
    return strTimeProp(start, end, '%I:%M %p', prop)
#type of truck method

def truckType(number):
	dict={1: 'F',2:'FT',3:'F',4:'V',5:'F',6:'FD',7:'F'}
	return dict[number]	
my_date=randomDate("1/1/2005", "1/1/2015", random.random())
my_time=randomTime("12:00 PM", "12:00 AM", random.random())
origin=random.choice(open("complete_city.csv").readlines()).strip()
destination=random.choice(open("complete_city.csv").readlines()).strip()
geolocator = Nominatim()
location_origin = geolocator.geocode(origin,exactly_one=True,timeout=10)
location_destination = geolocator.geocode(destination,exactly_one=True,timeout=10)
origin_long_lat=(location_origin.latitude,location_origin.longitude)
destination_long_lat=(location_destination.latitude,location_destination.longitude)
#print origin_long_lat
trip= int((vincenty(origin_long_lat,destination_long_lat).miles))
if(origin != destination):
	print "\""+my_time+"\","+"\""+my_date+"\","+"\""+truckType(random.randint(1,7))+"\","+"\""+"F"+"\","+"\""+" "+"\","+"\""+origin+"\","+"\""+str(trip)+"\","+"\""+destination+"\","+"\""+" "+"\","+"\""+"(111) 111-1111"+"\","+"\""+str(random.randint(80,100))+"\","+"\""+str(random.randint(30,40))+"\","+"\""+" "+"\","+"\""+str(random.randint(10,45))+"\","+"\""+"Company XXX"+"\","+"\""+" "+"\","+"\""+" "+"\","+"\""+" "+"\","+"\""+"R"+"\","+"\""+"A"+"\""


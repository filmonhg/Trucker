how data is engineered
----------------------
* time stamp is ranomized over period of 10 years
* Cities are generated from city data (http://www.city-data.com/) for cities
with population of 6000+. This is to make a list of cities in a good distribution
based around US and to make a good pick of city that has more transportation

* to get mile (distance) between cities geopy (python package) link (https://pypi.python.org/pypi/geopy)  is used
	-to install ==> sudo pip install geopy
	- the approach is that you first get the longitude and latitude of the address in a time out of 10 sec
	- and get Vincenty distance between them. I compared it with google map and it has shown very similar results
* then run python code from shell script to generate the fake data as big as you want them

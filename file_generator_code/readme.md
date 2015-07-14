how data is engineered
----------------------
* time stamp is ranomized over period of 10 years
* more than 20,000 US cities are randomly selected for origin and destination (data from http://www.city-data.com/)
 with a bias towards cities with population of 6000+. This helps in biased random pick of those major cities in
 the data as they have more busier truck transport than smaller cities.
* to get mile (distance) between cities geopy (python package) link (https://pypi.python.org/pypi/geopy)  is used
	- to install ==> sudo pip install geopy
	- the approach is that you first get the longitude and latitude of two cities (origin and destination)
	- get Vincenty distance (air distance in miles) between them because google API calls are limited and its hard
	  to generate big data in few days. Thus get approximate mileage using Vincenty distance and its very close to 
          what google API can provide and for the scope of the project it does not have to be precise.
* other attributes like load, truck type etc. are also generated randomly
* then run python code from shell script to generate the synthesized data as big as you want them
* for real time data source, the historical data is replayed (simulating real time data)

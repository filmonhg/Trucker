# Cassandra-Flask
app.py and cassie_utils.py should go on the node which you want to act as the web server.

Dependencies
```
sudo pip install flask cassandra-driver
```

Run the Flask webserver with the following
```
$ flask app.py
```

Here's a listing of the API calls which can be made now
-------------------------------------------------------------------------------------------------------------------
Fashion data schema
http://*web-server-public-ip*:5000/schema
-------------------------------------------------------------------------------------------------------------------
Get all records in the last N time increments
http://*web-server-public-ip*:5000/fashion/last/*N*/*TimeIncrement*/*Fields*

   <N> must be an integer
   <TimeIncrement> can be: seconds/minutes/hours/days/weeks
   <Fields> must be specified based on naming in the schema. If you want all fields, type 'all', otherwise type in the fields you want separated by '&' e.g. time&gender&store

   e.g http://52.25.158.196:3000/fashion/last/2/minutes/gender&store 

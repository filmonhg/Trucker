from flask import Flask, render_template, redirect, url_for, request, jsonify, json
from cassie_utils import CassieUtilities
import csv
import time
from datetime import datetime, timedelta
import time

app = Flask(__name__)

CUtils = CassieUtilities('52.8.124.34')
@app.route('/index')
def index():
    return render_template("refer.html",
				); 
@app.route('/realtime')
def realtime():
    user = {'nickname': 'Real Time Processing'}  # fake user
    city='Lake City'
    state='FL'
    result_outbound = CUtils.fetch_daterange(table='outbound_real_count',city=city,state=state)
    response = []
    for res in result_outbound:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})

    result_inbound = CUtils.fetch_daterange(table='inbound_real_count',city=city,state=state)
    in_response = []
    for res in result_inbound:
        in_response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
 
#    result_outbound = CUtils.fetch_daterange(table='outbound_real_count')
#    response = []
#    for res in result_outbound:
#        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})

#    result_inbound = CUtils.fetch_daterange(table='inbound_real_count')
#    in_response = []
#    for res in result_inbound:
#        in_response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
 
    result_outbound_state = CUtils.fetch_daterange_state(table='outbound_real_count_state')
    response_state = []
    for res in result_outbound_state:
        response_state.append({'state' : res[0], 'month_day' : res[1], 'count':res[2]}) 
    
    result_inbound_state = CUtils.fetch_daterange_state(table='inbound_real_count_state')
    in_response_state = []
    for res in result_inbound_state:
        in_response_state.append({'state' : res[0], 'month_day' : res[1], 'count':res[2]}) 
    result_lat_lng = CUtils.fetch_lat_lng(table='city_state_lat_lng',city=city,state=state)
    in_result_lat_lng = []
    for res in result_lat_lng:
	in_result_lat_lng.append({'city' : res[0], 'state' : res[1], 'lat':res[2],'lng':res[3]})
    return render_template("realtime.html",
				title='Real Time',
				user=user,
				posts=response,
				state_posts=response_state,
				in_posts=in_response,
				in_state_posts=in_response_state,
				in_lat_lng=in_result_lat_lng
				);



@app.route('/realtime', methods=['POST'])
def realtime_post():
    city = request.form['city']
    state= request.form['state']
    user = {'nickname': 'Real Time Processing'}  # fake user
    result_outbound = CUtils.fetch_daterange(table='outbound_real_count',city=city,state=state)
    response = []
    for res in result_outbound:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})

    result_inbound = CUtils.fetch_daterange(table='inbound_real_count',city=city,state=state)
    in_response = []
    for res in result_inbound:
        in_response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
 
    result_outbound_state = CUtils.fetch_daterange_state(table='outbound_real_count_state')
    response_state = []
    for res in result_outbound_state:
        response_state.append({'state' : res[0], 'month_day' : res[1], 'count':res[2]}) 
    
    result_inbound_state = CUtils.fetch_daterange_state(table='inbound_real_count_state')
    in_response_state = []
    for res in result_inbound_state:
        in_response_state.append({'state' : res[0], 'month_day' : res[1], 'count':res[2]}) 


    result_lat_lng = CUtils.fetch_lat_lng(table='city_state_lat_lng',city=city,state=state)
    in_result_lat_lng = []
    for res in result_lat_lng:
	in_result_lat_lng.append({'city' : res[0], 'state' : res[1], 'lat':res[2],'lng':res[3]})
    return render_template("realtime.html",
				title='Real Time',
				user=user,
				posts=response,
				state_posts=response_state,
				in_posts=in_response,
				in_state_posts=in_response_state,
				city=city,
				state=state,
				in_lat_lng=in_result_lat_lng
				);



@app.route('/batch')
def batch():
    yr='2014'
    user = {'nickname': 'Batch Processing'}  # fake user
    #result_outbound = CUtils.fetch_daterange(table='outbound_city_state_major')
    result_outbound = CUtils.fetch_major_by_year(table='outbound_city_state_major',year=yr)
    result_inbound = CUtils.fetch_major_by_year(table='inbound_city_state_major',year=yr)
    result_instate = CUtils.fetch_state_by_year(table='inbound_state',year=yr)
    result_outstate = CUtils.fetch_state_by_year(table='outbound_state',year=yr)
    print result_instate;
    print result_outstate;
    response = []
    response2 = []
    in_response = []
    out_response = []
    print "+++++++++++++++"
    for res in result_outbound:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        response.append({'year': res[0], 'city' : res[1], 'state' : res[2], 'count':res[3]})

    for res in result_inbound:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        response2.append({'year': res[0], 'city' : res[1], 'state' : res[2], 'count':res[3]})
    for res in result_outstate:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        out_response.append({'year': res[0], 'state' : res[1], 'count':res[2]})
    print "out"
    print res[2]
    print "----"
    for res in result_instate:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        in_response.append({'year': res[0], 'state' : res[1], 'count':res[2]})
    
    print "in"
    print res[2]
    print "----"
    return render_template("batch.html",
                                title='Batch Time',
                                user=user,
                                posts=response,
				posts2=response2,
				in_state=in_response,
				out_state=out_response,
				year=yr
                                );

@app.route('/batch', methods=['POST'])
def batch_post():
    year = request.form["year"]
    result_outbound = CUtils.fetch_major_by_year(table='outbound_city_state_major',year=year)
    result_inbound = CUtils.fetch_major_by_year(table='inbound_city_state_major',year=year)
    result_instate = CUtils.fetch_state_by_year(table='inbound_state',year=year)
    result_outstate = CUtils.fetch_state_by_year(table='outbound_state',year=year)
    print result_instate;
    print result_outstate;
    response = []
    response2 = []
    in_response = []
    out_response = []

    for res in result_outbound:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        response.append({'year': res[0], 'city' : res[1], 'state' : res[2], 'count':res[3]})

    for res in result_inbound:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        response2.append({'year': res[0], 'city' : res[1], 'state' : res[2], 'count':res[3]})
    for res in result_outstate:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        out_response.append({'year': res[0], 'state' : res[1], 'count':res[2]})
    print "out"
    print res[2]
    print "----"
    for res in result_instate:
        #response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
        in_response.append({'year': res[0], 'state' : res[1], 'count':res[2]})

    return render_template("batch.html",
                                title='Batch Time',
                                posts=response,
				posts2=response2,
				in_state=in_response,
				out_state=out_response,
				year=year
                                );
#
#
@app.route('/map')
def map():
    result_outbound = CUtils.fetch_daterange(table='outbound_real_count')
    response = []
    print result_outbound
    for res in result_outbound:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]}) 
    return render_template("test.html",
				title='Map data',
				posts=response
				);
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

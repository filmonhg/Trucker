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
    user = {'nickname': 'Real Time Processing'}  # fake user
    result_outbound = CUtils.fetch_daterange(table='outbound_real_count')
    response = []
    for res in result_outbound:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]})
    return render_template("realtime.html",
				user=user,
                                posts=response
				); 
@app.route('/realtime')
def realtime():
    user = {'nickname': 'Real Time Processing'}  # fake user
    result_outbound = CUtils.fetch_daterange(table='outbound_real_count')
    response = []
    for res in result_outbound:
        response.append({'city': res[0], 'state' : res[1], 'year' : res[2], 'count':res[3]}) 
    return render_template("realtime.html",
				title='Real Time',
				user=user,
				posts=response
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

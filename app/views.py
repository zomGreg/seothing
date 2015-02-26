from app import app
import json
from flask import render_template
import datetime
import os

@app.route('/google')
def google():
    with open('./tmp/google.json', 'r') as f:
        google_data=json.loads(f.read())
        google_results = google_data['google']
        last_update = os.path.getmtime('./tmp/google.json')
        last_update = datetime.datetime.fromtimestamp(last_update)
        return render_template("google.html",
                               google_results=google_results,
                               last_update=last_update)

@app.route('/yahoo')
def yahoo():
    with open('./tmp/yahoo.json', 'r') as f:
        yahoo_data=json.loads(f.read())
        yahoo_results = yahoo_data['yahoo']
        last_update = os.path.getmtime('./tmp/yahoo.json')
        last_update = datetime.datetime.fromtimestamp(last_update)
        return render_template("yahoo.html",
                               yahoo_results=yahoo_results,
                               last_update=last_update)

@app.route('/bing')
def bing():
    with open('./tmp/bing.json', 'r') as f:
        bing_data=json.loads(f.read())
        bing_results = bing_data['bing']
        last_update = os.path.getmtime('./tmp/bing.json')
        last_update = datetime.datetime.fromtimestamp(last_update)
        return render_template("bing.html",
                               bing_results=bing_results,
                               last_update=last_update)

@app.route('/')
@app.route('/index')
def index():
    all=[]
    all_dict={}
    with open('./tmp/google.json', 'r') as fg:
        google_data=json.loads(fg.read())
        google_results = google_data['google']

    with open('./tmp/yahoo.json', 'r') as fy:
        yahoo_data=json.loads(fy.read())
        yahoo_results = yahoo_data['yahoo']

    with open('./tmp/bing.json', 'r') as fb:
        bing_data=json.loads(fb.read())
        bing_results = bing_data['bing']

        last_update = os.path.getmtime('./tmp/bing.json')
        last_update = datetime.datetime.fromtimestamp(last_update)

    return render_template("index.html",
                           google_results=google_results,
                           yahoo_results=yahoo_results,
                           bing_results=bing_results,
                           last_update=last_update)

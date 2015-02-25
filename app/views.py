from app import app
import json
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/google')
def test():
    with open('./tmp/google.json', 'r') as f:
        google_data=json.loads(f.read())
        google_results = google_data['google']
        # search_terms = [str(i['search_term']) for i in google_data['google']]
        # dell_results = [str(i['results']['dell.com']) for i in google_data['google']]
        # enstratius_results = [str(i['results']['enstratius.com']) for i in google_data['google']]
        return render_template("google.html",
                               google_results=google_results)


@app.route('/results')
def results():
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

    return render_template("results.html",
                           google_results=google_results,
                           yahoo_results=yahoo_results,
                           bing_results=bing_results)

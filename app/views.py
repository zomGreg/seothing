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
        # return json.dumps(google_data)
        results = google_data['google']
        search_terms = [str(i['search_term']) for i in google_data['google']]
        dell_results = [str(i['results']['dell.com']) for i in google_data['google']]
        enstratius_results = [str(i['results']['enstratius.com']) for i in google_data['google']]
        return render_template("google.html",
                               results=results)

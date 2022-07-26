from flask import Flask, render_template, redirect
import os
from datetime import date
import urllib
import json

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    # Contacting API
    key = os.environ['VC_API_KEY']
    city = 'nairobi'
    start = '2022-01-01'
    end = date.today().strftime('%Y-%m-%d')
    try:
        ResultBytes = urllib.request.urlopen(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/capetown/2021-12-01/2022-01-01?unitGroup=metric&elements=datetime%2Ctemp&include=days%2Cobs&key={key}&contentType=json')
        data = json.loads(ResultBytes.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        ErrorInfo = e.read().decode() 
        data = ErrorInfo
    return render_template('index.html', data=data)
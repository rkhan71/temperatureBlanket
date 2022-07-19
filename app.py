from flask import Flask, render_template, redirect
import os
import requests
import arrow

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    # Contacting API
    start = arrow.get('2022-07-19')
    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params = {
            'lat': 1.2921,
            'lng': 36.8219,
            'params': 'airTemperature',
            'start': start.to('UTC').timestamp(),
            'end': start.shift(days=1).to('UTC').timestamp()
        },
        headers = {
            'Authorization': os.environ['SG_API_KEY']
        }
    )
    data = response.json()
    return render_template('index.html', data=data)
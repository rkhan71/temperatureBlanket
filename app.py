from flask import Flask, render_template, redirect, request
import os
import urllib
import json

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Make sure full form submitted
        if not request.form.get('city'):
            return render_template('index.html')
        if not request.form.get('year'):
            return render_template('index.html')
        try:
            year = int(request.form.get('year'))
            if year < 1980 or year > 2021:
                return render_template('index.html')
        except:
            return render_template('index.html')
        city = request.form.get('city')
        start = request.form.get('year') + '-01-01'
        end = request.form.get('year') + '-01-31'

        # Get data from API 
        key = os.environ['VC_API_KEY']
        try:
            ResultBytes = urllib.request.urlopen(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city.replace(' ', '%20')}/{start}/{end}?unitGroup=metric&elements=datetime%2Ctemp&include=days%2Cobs%2Cremote&key={key}&options=nonulls&contentType=json")
            data = json.loads(ResultBytes.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            # Incase of error (usually running out of credit to use API) pass in error message
            ErrorInfo = e.read().decode() 
            return render_template('index.html', error=ErrorInfo)
        
        # Extract the useful data from the API data
        temps = [float(i['temp']) for i in data['days']]
        addy = data['resolvedAddress']

        # Pass in relevant data
        return render_template('index.html', year=year, temps=temps, addy=addy)
    else:
        return render_template('index.html')
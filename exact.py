import requests
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request

app = Flask(__name__)

load_dotenv() 
api_key = os.getenv('API_KEY')



@app.route('/')
def home():
    return render_template('weather.html')

@app.route('/results', methods=['POST'])
def render_results():
    city_name = request.form ['cityName']
    wdata = check_weather(city_name,api_key)
    temp = "{0:.2f}".format(wdata["main"]["temp"])
    feels = "{0:.2f}".format(wdata["main"]["feels_like"])
    atmos = wdata["weather"][0]["description"]
    located = wdata["name"]
    return render_template('results.html',temperature=temp,feelsLike=feels,atmosphere=atmos,location=located)

def check_weather(city_name,apiKey):
    apiUrl = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(city_name,apiKey)
    r = requests.get(apiUrl)
    return r.json()
app.run(debug=True)

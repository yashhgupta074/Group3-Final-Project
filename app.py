import requests
import atexit 
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
from flask import Flask, render_template, request
import time

app = Flask(__name__)
client = MongoClient("mongodb+srv://yashgupta074:Asdf%401234@cluster0.mwp62si.mongodb.net/?retryWrites=true&w=majority")
db = client.Weather_Dashboard_data

r1 = requests.get("http://api.weatherapi.com/v1/forecast.json?key=4797fb004a3a483b84e105801231104&q=Chicago&days=7&aqi=no&alerts=no")
r3 = requests.get("http://api.weatherapi.com/v1/forecast.json?key=4797fb004a3a483b84e105801231104&q=Dubai&days=7&aqi=no&alerts=no")
r2 = requests.get("http://api.weatherapi.com/v1/forecast.json?key=4797fb004a3a483b84e105801231104&q=Delhi&days=7&aqi=no&alerts=no")
r4 = requests.get("http://api.weatherapi.com/v1/forecast.json?key=4797fb004a3a483b84e105801231104&q=Paris&days=7&aqi=no&alerts=no")
r5 = requests.get("http://api.weatherapi.com/v1/forecast.json?key=4797fb004a3a483b84e105801231104&q=Toronto&days=7&aqi=no&alerts=no")
r6 = requests.get("http://api.weatherapi.com/v1/forecast.json?key=4797fb004a3a483b84e105801231104&q=Rome&days=7&aqi=no&alerts=no")



def data_load():
    #while True:
    if r1.status_code == 200:
        Chicago = r1.json()
        #time.sleep(60)
    else:
        exit()
    if r2.status_code == 200:
        Dubai = r2.json()
        #time.sleep(60)
    else:
        exit()
    if r3.status_code == 200:
        Delhi = r3.json()
        #time.sleep(60)
    else:
        exit()
    if r4.status_code == 200:
        Paris = r4.json()
        #time.sleep(60)
    else:
        exit()
    if r5.status_code == 200:
        Toronto = r5.json()
        #time.sleep(60)
    else:
        exit()
    if r6.status_code == 200:
        Rome = r6.json()
        #time.sleep(60)
    else:
        exit()    
    db.final2.insert_one(Chicago)
    db.final2.insert_one(Delhi)
    db.final2.insert_one(Dubai)
    db.final2.insert_one(Paris)
    db.final2.insert_one(Toronto)
    db.final2.insert_one(Rome)

data_load()

scheduler = BackgroundScheduler()
scheduler.add_job(func=data_load, trigger="interval", hours=24)
scheduler.start()

@app.route('/')
def homepage():
    Chicago = r1.json()
    date1=Chicago['forecast']['forecastday']
    Dubai = r2.json()
    Paris = r3.json()
    Delhi = r4.json()
    Toronto = r5.json()
    Rome = r6.json()

    return render_template('homepage.html', **locals())

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
    name = request.form['cityname']
    data = get_weather_results(name)
    return render_template('results.html',data=data)


def get_weather_results(name):
    api_url = "http://api.weatherapi.com/v1/forecast.json?key=4797fb004a3a483b84e105801231104&q={}&days=7&aqi=no&alerts=no".format(name)
    r = requests.get(api_url)
    return r.json()


if __name__ == '__main__':
    app.run(debug=True)

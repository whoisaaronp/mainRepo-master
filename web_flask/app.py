from flask import Flask, render_template
from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://juniha:Rodyroem@cluster0-shard-00-00-naqor.mongodb.net:27017,cluster0-shard-00-01-naqor.mongodb.net:27017,cluster0-shard-00-02-naqor.mongodb.net:27017/covid_ontario?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo = PyMongo(app)

# time filter
@app.template_filter('strftime')
def _jinja2_filter_datetime(date,fmt=None):
    date = datetime.fromtimestamp(date)
    native = date.replace(tzinfo=None)
    format = '%Y-%m-%d'
    return native.strftime(format)

@app.route('/')
def home():
    status = mongo.db.status
    status_data = []
    for s in status.find().sort("date"):
        status_data.append({
            'date': _jinja2_filter_datetime(int(s.get('date'))),
            'deceased': s.get('deceased',0),
            'confirmed': s.get('confirmed',0),
            'resolved': s.get('resolved',0),
            'pending': s.get('pending',0),
            'total': s.get('total',0),
        })

    return render_template('home.html',ontario_data=status_data)

# set up your route
@app.route('/fetch')
def index():
    status = mongo.db.status
    status_data = []
    for s in status.find().sort("date"):
        status_data.append({
            'date': _jinja2_filter_datetime(int(s.get('date'))),
            'deceased': s.get('deceased',0),
            'confirmed': s.get('confirmed',0),
            'resolved': s.get('resolved',0),
            'pending': s.get('pending',0),
            'total': s.get('total',0),
        })

    return render_template('fetch.html',ontario_data=status_data)

# set up your barchart
@app.route('/bar_chart')
def bar_chart():
    return render_template('barchart.html')

# set up your linechart
@app.route('/line_chart')
def line_chart():
    return render_template('linechart.html')

# set up your piechart
@app.route('/pie_chart')
def pie_chart():
    return render_template('piechart.html')

# set up your bubblechart
@app.route('/bubble_chart')
def bubble_chart():
    return render_template('bubblechart.html')


@app.route('/fetch')
def fetch():
    params = {
        'spider_name': 'ontario',
        'start_requests': True

    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    # fetch_result = json.loads(response.text)
    # return render_template('fetch.html', content=fetch_result)
    return response.text

    
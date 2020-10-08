from flask import Flask, render_template
import json
# import requests
from datetime import datetime


app = Flask(__name__)
# mongodb+srv://juniha:Rodyroem@cluster0-naqor.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true

# set up your route
@app.route('/')
def index():
	return render_template('home.html')

# set up your barchart
@app.route('/bar-chart')
def bar_chart():
	return render_template('barchart.html')

# set up your linechart
@app.route('/line-chart')
def line_chart():
	return render_template('linechart.html')

# set up your piechart
@app.route('/pie-chart')
def pie_chart():
	return render_template('piechart.html')

# set up your bubblechart
@app.route('/bubble-chart')
def bubble_chart():
	return render_template('bubblechart.html')


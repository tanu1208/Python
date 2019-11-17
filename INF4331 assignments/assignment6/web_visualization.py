#!/usr/bin/env python3

"""
Simple web application for presenting CO2, 
temperature data and country data plots.

Usage:
python3 web_visualization.py

"""

import temperature_CO2_plotter as tcp
import sys
from flask import Flask, render_template, request, send_file

CO2_file="static/CO2_plot.svg"
temperature_file="static/temperature.svg"
CO2_by_country_file="static/CO2_by_country.svg"
uio_file="static/uio.png"

app = Flask(__name__)

#################### Routing ####################
#for redirecting properly, to handle more cases

@app.route("/")
def start():
	return render_template("index.html", uio_file=uio_file, CO2_file=CO2_file)

@app.route("/temperature")
def temperature():
	return render_template("temperature.html", uio_file=uio_file, temperature_file=temperature_file)

@app.route("/CO2_by_country")
def CO2_by_country():
	return render_template("CO2_by_country.html", uio_file=uio_file, CO2_by_country=CO2_by_country_file)

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/help/matplotlib.pyplot")
def matplot_help():
    return render_template("matplotlib.pyplot.html")

@app.route("/help/help_sys")
def help_sys():
    return render_template("sys.html")

@app.route("/help/pandas")
def pandas_help():
    return render_template("pandas.html")

@app.route("/help/flask")
def flask_help():
    return render_template("flask.html")

#needed to route files also, because flask was overwriting simple hrefs

@app.route("/help/temperature_CO2_plotter")
def download_plot():
    return send_file("temperature_CO2_plotter.py")

@app.route("/help/CO2_by_country")
def download_country():
    return send_file("data/CO2_by_country.csv", attachment_filename="CO2_by_country.csv")

@app.route("/help/co2")
def download_co2():
    return send_file("data/co2.csv", attachment_filename="co2.csv")

@app.route("/help/temperature")
def download_temp():
    return send_file("data/temperature.csv", attachment_filename="temperature.csv")

#################### Posting ####################

@app.route('/index_changed', methods=['POST'])
def index_changed():
	year_from = int(request.form["time_from"])
	year_to = int(request.form["time_to"])
	yaxis_min_CO2 = int(request.form.get("y_min_CO2"))
	yaxis_max_CO2 = int(request.form.get("y_max_CO2"))

	tcp.plot_CO2(ymin=yaxis_min_CO2, ymax=yaxis_max_CO2, start_year=year_from, end_year=year_to)

	return render_template("index.html", uio_file=uio_file, CO2_file=CO2_file)

@app.route("/temperature_changed", methods=['POST'])
def temperature_changed():
	year_from = int(request.form["time_from"])
	year_to = int(request.form["time_to"])
	yaxis_min_temperature = int(request.form.get("y_min_temperature"))
	yaxis_max_temperature = int(request.form.get("y_max_temperature"))
	month_to_predict = str(request.form.get("month"))

	tcp.plot_temperature(ymin=yaxis_min_temperature, ymax=yaxis_max_temperature, start_year=year_from, end_year=year_to, month=month_to_predict)

	return render_template("temperature.html", uio_file=uio_file, temperature_file=temperature_file)

@app.route('/CO2_by_country_changed', methods=['POST'])
def CO2_by_country_changed():
	time = int(request.form["time"])
	l_treshold = float(request.form.get("min"))
	u_treshold = float(request.form.get("max"))

	tcp.plot_CO2_by_Country(year=time, lower_treshold=l_treshold, upper_treshold=u_treshold)

	return render_template("CO2_by_country.html", uio_file=uio_file, CO2_by_country=CO2_by_country_file)

#################### Cache fix ####################

@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

if __name__ == "__main__":
	app.run(debug=True)
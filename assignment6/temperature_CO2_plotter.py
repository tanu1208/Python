#!/usr/bin/env python3

"""
Program that reads data from CO2.csv, temperature.csv and CO2_by_country.csv,
then generates a labeled, nice plot of time vs. CO2, time vs. temperature, 
and CO2 emissions per capita for different countries.

Usage:
python3 temperature_CO2_plotter.py
"""

import sys
import matplotlib.pyplot as plt
import pandas as pd


#importing the files that are going to be used in this assignment
CO2_file="data/co2.csv"
temperature_file="data/temperature.csv"
CO2_by_contry_file="data/CO2_by_country.csv"

def plot_CO2(ymin=0, ymax=10000, start_year=1751, end_year=2012):
	"""
		Method for reading CO2 file with the help of the read_csv 
		method provided by pandas. 
		@param start_year - the start year specified
		@param end_year - the end year specified
		@param ymin - Lowest y-axis value to plot
		@param ymax - highest y-axis value to plot
		Setting default params
	"""

	co2_info = pd.read_csv(CO2_file)
	year = []
	carbon_level = []

	for i in zip(co2_info['Year'], co2_info['Carbon']):
		if (i[0] >= start_year) and (i[0] <= end_year):
			year.append(i[0])
			carbon_level.append(i[1])

	plt.close(0) #needed when plotting multiple figures
	plt.figure(0) #needed when plotting multiple figures
	plt.plot(year, carbon_level)
	plt.xlabel("Year")
	plt.ylabel("Carbon emissions")
	plt.ylim(ymin, ymax)
	plt.savefig("static/CO2_plot.svg")

def plot_temperature(ymin=-6, ymax=5, start_year=1816, end_year=2012, month="July"):
	"""
		Method for reading temperature file with the help of 
		the read_csv method provided by pandas. 
		@param start_year - the start year specified
		@param end_year - the end year specified
		@param month - for illustrating
		@param ymin - Lowest y-axis value to plot
		@param ymax - highest y-axis value to plot
		Setting default params
	"""

	temp_info = pd.read_csv(temperature_file)
	year = []
	temperature = []

	for i in zip(temp_info['Year'], temp_info[month]):
		if (i[0] >= start_year) and (i[0] <= end_year):
			year.append(i[0])
			temperature.append(i[1])

	plt.close(1) #needed when plotting multiple figures
	plt.figure(1) #needed when plotting multiple figures
	plt.plot(year, temperature)
	plt.xlabel("Year")
	plt.ylabel("Temperature")
	plt.title(month)
	plt.ylim(ymin, ymax)
	plt.savefig("static/temperature.svg")

def plot_CO2_by_Country(year=1960, lower_treshold=5.0, upper_treshold=30.0):
	"""
		Method for reading co2 values based on country and year
		using pandas. Then using country abbreviation to plot with 
		co2 level based on the chosen year.
		@param year - The year to plot co2 emission for all countries
		@param lower_treshold - Value for min emission to plot
		@param upper_treshold - Value for max emission to plot
	"""
	plt.close(2) #needed when plotting multiple figures
	plt.figure(2) #needed when plotting multiple figures

	#Another way of setting up the dataframe, with (a lot of) help from pandas framweork
	co2_country_info = pd.read_csv(CO2_by_contry_file) #reading the csv file and creates a dataframe with values
	co2_country_info = co2_country_info.set_index(co2_country_info[co2_country_info.columns[1]]) #setting country abbreviation as index
	co2_country_info = co2_country_info[co2_country_info[str(year)] >= lower_treshold] #filtering out years below lower_treshold
	co2_country_info = co2_country_info[co2_country_info[str(year)] <= upper_treshold] #filtering out years over upper_treshold
	
	co2_country_info.loc[:, str(year)].plot(kind="bar") #locking the values to be everything until the years, and the year to be used

	plt.title("CO$_2$ emissions in year {}, for countries within the interval [{}, {}] \n".format(year, lower_treshold, upper_treshold)) #setting the title
	plt.ylabel("CO$_2$ emission, tons per capital")
	plt.savefig("static/CO2_by_country.svg", bbox_inches="tight")

if __name__=="__main__":
	#plot_CO2()
	#plot_temperature()
	plot_CO2_by_Country()

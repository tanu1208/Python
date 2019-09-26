# [INF4331](https://github.com/UiO-INF3331/INF4331-tanusanr) - Assignment 6

Web programming and data analysis

## How to run the files
The [data](https://github.com/UiO-INF3331/INF4331-tanusanr/tree/master/assignment6/data) folder contains the csv files that should be used for values.

### Task 6.1 & 6.4 - [temperature_CO2_plotter.py](https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment6/temperature_CO2_plotter.py)
This just runs the file and creates 3 plots, one for each csv file. You can specify plots inside the file or it will run default values.
```
python3 temperature_CO2_plotter.py
```

### Task 6.2, 6.3 & 6.5 - [web_visualization.py](https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment6/web_visualization.py)
This runs the flask file which creates the user interface based on the html files. 
There is a nice layout with navigation and image of the plot.
```
python3 web_visualization.py
```

<p align="center">
  <img width="100%" src="https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment6/screenshots/startPage.png">
  <br>
  Startpage with information about CO<sub>2</sub> emission for a given year.
</p>

<p align="center">
  <img width="100%" src="https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment6/screenshots/temp.png">
  <br>
  Page for viewing temperature for a given year based on month.
</p>

<p align="center">
  <img width="100%" src="https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment6/screenshots/co2_country.png">
  <br>
  Page for viewing CO<sub>2</sub> emission from various countries for a given year within a user specified bound.
</p>

<p align="center">
  <img width="100%" src="https://github.com/UiO-INF3331/INF4331-tanusanr/blob/master/assignment6/screenshots/help.png">
  <br>
  Page for viewing information about the methods and hos to use them.
</p>

## Built With

* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) - Flask is a microframework for Python to create an interface.
* [Matplotlib.pyplot](https://matplotlib.org/3.0.2/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) - Used for plotting the graphs
* [Flask](http://flask.pocoo.org/docs/1.0/) - Used for randomly selecting color for grep

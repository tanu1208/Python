#!/usr/bin/env python3
# Calculate and writes an image of the Mandelbrot set with the help of numpy.

from matplotlib import pyplot as plt;
from numpy import linspace, empty;
import time;
import warnings;

def mandelbrot(complexNum, max_iteration):
    #returning null if the vaule is in the mandelbrot set, if not it returns the steps before exiting
	
    #creating variables to use in the loops, to easier see what is happening
	compLen = len(complexNum);
	compLenFirst = len(complexNum[0]);

	totalIterations = empty((compLen, compLenFirst)); #creating an empty array to hold the total iterations
	reslen = len(totalIterations);
	resLenFirst = len(totalIterations[0]);

	z = empty((compLen, compLenFirst));

	for iterations in range(max_iteration):
		z = z**2 + complexNum;
		for x in range(reslen):
			for y in range(resLenFirst):
				if abs(z[x][y]) > 2:
					totalIterations[x][y] = iterations; #not in the mandelbrot set

	#checking if the number in totalIterations is 0 to return because it is in the mandelbrot set 
	for i in range(reslen):
		for j in range(resLenFirst):
			if totalIterations[i][j] == 0:
				totalIterations[i][j] = None;

	return totalIterations;

def mandelbrot_check(startX, endX, startY, endY, width, height, max_iteration):
	#setting up the matrix and adding the values into the matrix. 
	xaxis = linspace(startX, endX, width);
	yaxis = linspace(startY,  endY, height);
	values = empty((width, height), dtype=complex);

	for x in range(width):
		for y in range(height):
			values[y,x] = xaxis[x] + 1j * yaxis[y];

	values = mandelbrot(values, max_iteration);
	return (xaxis, yaxis, values);

def draw(X, Y, values):
    # modifying the colormap to color the points in the mandelbrot set to black
    modifiedColorMap = plt.cm.gnuplot2;
    modifiedColorMap.set_bad(color='black', alpha=None);
    plt.imshow(values, cmap = modifiedColorMap, extent = (X.min(), X.max(), Y.min(), Y.max()));
    plt.xlabel("Real");
    plt.ylabel("Imaginary");
    plt.savefig("pictures/mandelbrot_plot2.png");


if __name__ == "__main__":
	warnings.filterwarnings("ignore") #to ignore runtime warning
    # The values can be adjusted
	width = 1000;
	height = 1000;
	max_iteration = 80;
	yMin = -1.18;
	yMax = 1.5;
	xMin = -2.18;
	xMax = 0.5;
	t1 = time.clock();
	# Here we calculate, write the result to an image and printing out the time in the terminal.
	result = mandelbrot_check(xMin, xMax, yMin, yMax, width, height, max_iteration);
	t2 = time.clock();
	print('{:.3f} sec'.format(t2-t1));
	draw(result[0], result[1], result[2]);


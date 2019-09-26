#!/usr/bin/env python3
# Calculate and writes an image of the Mandelbrot set with manual calculation.

from matplotlib import pyplot as plt;
from numpy import linspace, empty;
import time;

def mandelbrot(complexNum, max_iteration):
    #returning null if the vaule is in the mandelbrot set, if not it returns the steps before returning
	z=0;
	for iteration in range(max_iteration):
		if abs(z) > 2:
			return iteration;
		z = z**2 + complexNum;
	return None

def mandelbrot_check(startX, endX, startY, endY, width, height, max_iteration):
	#setting up the matrix and adding the values into the matrix with linspace. 
	xaxis = linspace(startX, endX, width);
	yaxis = linspace(startY,  endY, height);
	values = empty((width, height));

	for y in range(width):
		for x in range(height):
			values[y,x] = mandelbrot((xaxis[x] + 1j * yaxis[y]), max_iteration);
	return (xaxis, yaxis, values);

def draw(X, Y, values):
    # modifying the colormap to color the points in the mandelbrot set to black
    modifiedColorMap = plt.cm.gnuplot;
    modifiedColorMap.set_bad(color='black', alpha=None);
    plt.imshow(values, cmap = modifiedColorMap, extent = (X.min(), X.max(), Y.min(), Y.max()));
    plt.xlabel("Real");
    plt.ylabel("Imaginary");
    plt.savefig("pictures/mandelbrot_plot.png");


if __name__ == "__main__":
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


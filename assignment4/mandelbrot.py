#!/usr/bin/env python3
# This is the user interface for the mandelbrot program and how to show the different methods

from matplotlib import pyplot as plt
import time
import sys
import mandelbrot_1 as m1
import mandelbrot_2 as m2
import mandelbrot_3 as m3
from cython.mandelbrot_4_cython import mandelbrot_check as mc

def draw(X, Y, values, filename="mandelbrot_plot.png", colormap="gnuplot"):
    # modifying the colormap to color the points in the mandelbrot set to black
    modifiedColorMap = plt.get_cmap(colormap);
    modifiedColorMap.set_bad(color='black', alpha=None);
    modifiedColorMap.set_under(color='black', alpha=None);
    plt.imshow(values, cmap = modifiedColorMap, extent = (X.min(), X.max(), Y.min(), Y.max()));
    plt.xlabel("Real");
    plt.ylabel("Imaginary");
    plt.savefig(filename);


def help():
    print("\nusage: python3 mandelbrot.py");
    print("a list will pop up, asking for each value, if the value is empty it will be set to default. \n");
    print("Options: ");
    print("filename           : name of the printed image, in png format");
    print("xMin/xmin          : minimum x-coordinate, to start drawing the x-axis from");
    print("xMax/xmax          : maximum x-coordinate to end drawing the x-axis");
    print("yMin/ymin          : minimum y-coordinate, to start drawing the y-axis from");
    print("yMax/ymax          : maximum y-coordinate, to end drawing the y-axis");
    print("width              : width for the scaling");
    print("height             : height for the scaling");
    print("implementation     : implementation/program to use, range from 1 to 4");
    print("iteration          : number of iterations through mandelbrot function before concluding its in the set");
    print("cmap               : colormap to use when drawing the plot, default: gnuplot");
    sys.exit()

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None):
    # this function returns true if one or more points are in the mandelbrot set.
    # and returns false if the rectangle is entirely outside the mandelbrot set.
    # checking if the absolute value of xmin and ymin is over 2 og the absolute value of the xmax and ymax is below -2
    # if they are, that means it is outside of the mandelbrot set, else I compyte the result and draw the image if the user gives a filename


    if (abs(xmin + ymin * 1j) > 2) or (abs(xmax + ymax * 1j) < -2): 
        return False;

    result = m3.mandelbrot_check(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time);
    if plot_filename != None:
        draw(X=result[0], Y=result[1], values=result[2], filename=plot_filename);
        
    return True;



if __name__ == "__main__":

    #default values:
    width = 1000;
    height = 1000;
    max_iteration = 80;
    yMin = -1.18;
    yMax = 1.5;
    xMin = -2.18;
    xMax = 0.5;
    implementation = 3;
    cMap="gnuplot";
    filename = "mandelbrot_plot.png";

    arguments = sys.argv[1:];

    if len(arguments) > 0 and arguments[0] == "--help":
        help();

    while True:
        userInputFile = input("Type in the filename: ");
        if(len(userInputFile) > 0):
            filename = userInputFile.strip();
        else:
            filename = "mandelbrot_plot.png";

        userInputXmin = input("Type in the xMin: ");
        if(len(userInputXmin) > 0):
            xMin = float(userInputXmin.strip());
        else:
            xMin = -2.18;

        userInputXmax = input("Type in the xMax: ");
        if(len(userInputXmax) > 0):
            xMax = float(userInputXmax.strip());
        else:
            xMax = 0.5;

        userInputYmin = input("Type in the yMin: ");
        if(len(userInputYmin) > 0):
            yMin = float(userInputYmin.strip());
        else:
            yMin = -1.18;

        userInputYmax = input("Type in the yMax: ");
        if(len(userInputYmax) > 0):
            yMax = float(userInputYmax.strip());
        else:
            yMax = 1.5;

        userInputWidth = input("Type in the width: ");
        if(len(userInputWidth) > 0):
            width = int(userInputWidth.strip());
        else:
            width = 1000;

        userInputHeight = input("Type in the height: ");
        if(len(userInputHeight) > 0):
            height = int(userInputHeight.strip());
        else:
            height = 1000;

        userInputImplementation = input("Type in the implementation: ");
        if(len(userInputImplementation) > 0):
            implementation = int(userInputImplementation.strip());
        else:
            implementation = 3;

        userInputIteration = input("Type in the maximum iterations: ");
        if(len(userInputIteration) > 0):
            max_iteration = int(userInputIteration.strip());
        else:
            max_iteration = 1000;


        print("\ncolormap suggestions: [gnuplot, gnuplot2, hsv, gist_rainbow, gist_ncar, nipy_spectral, prism, gist_stern, etc]")
        userInputCmap = input("Type in the colormap to use for the plot: ");
        if(len(userInputCmap) > 0):
            cMap = userInputCmap.strip();
        else:
            cMap = "gnuplot";

        break;


    t1 = time.clock()
    # Here we do the calculations and write the resulting image.
    if implementation == 1:
        result = m1.mandelbrot_check(xMin, xMax, yMin, yMax, width, height, max_iteration);
    elif implementation == 2:
        result = m2.mandelbrot_check(xMin, xMax, yMin, yMax, width, height, max_iteration);
    elif implementation == 3:
        result = m3.mandelbrot_check(xMin, xMax, yMin, yMax, width, height, max_iteration);
    elif implementation == 4:
        result = mc(xMin, xMax, yMin, yMax, width, height, max_iteration);
    else:
        result = m3.mandelbrot_check(xMin, xMax, yMin, yMax, width, height, max_iteration);

    t2 = time.clock()
    print('mandelbrot_'+str(implementation)+ ' took '+'{:.3f} sec'.format(t2-t1))
    draw(X=result[0], Y=result[1], values=result[2], filename=filename, colormap=cMap)



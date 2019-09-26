#!/usr/bin/env python3

from numpy import ones, full, array_equal, int16, asarray
from mandelbrot import compute_mandelbrot
#import mandelbrot_1 as m1
#import mandelbrot_2 as m2
#import mandelbrot_3 as m3
#from cython import mandelbrot_4_cython as m4

#easy test cases, just checking one which is totally outside and within the mandelbrot set

def test_compute_mandelbrot():
	#test case for numbers totally outside of the mandelbrot set
	assert compute_mandelbrot(3.0, 4.0, 3.0, 4.0, 200, 200, 1000, None) == False;

def test_entirely_inside_mandelbrotSet():
	#test case for numbers within the mandelbrot set
	assert compute_mandelbrot(-0.50, 0.0, -0.20, 0.20, 200, 200, 1000, None) == True;


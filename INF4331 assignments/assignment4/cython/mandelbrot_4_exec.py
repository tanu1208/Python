import mandelbrot_4_cython
import os

os.system('python3 mandelbrot_4_setup.py build_ext --inplace'); #to build the cython file

mandelbrot_4_cython.main(); #run the method to see if it works
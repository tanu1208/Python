# [INF4331](https://github.com/UiO-INF3331/INF4331-tanusanr) - Assignment 4

Calculating if a complex number is in the mandelbrot set with python and cython programming.

## Getting Started

There is a setup file to be ran before running the programs. How to run:

```
sudo python3 setup.py install
```

## Running the tests

The tests is run automatically when you run the command below:

```
py.test
```

### Info
You can run every file independently or with the main file that contains the interface. To test the cython implementation you can use the mandelbrot_4_exec file to compile and run this implementation.

```
python3 mandelbrot_1.py #python

python3 mandelbrot_2.py #numpy

python3 mandelbrot_3.py #numba

python3 mandelbrot_4_exec.py #cython

python3 mandelbrot.py #main file
```


### Test cases

There are only two test cases, because the tast stated two cases. One where the numbers are completely in the mandelbrot set. And another case is just a random number which is entirely outside the mandelbrot set.

I created the compute_mandelbrot to test if it was inside the set or not, after one of the the teaching assistants posted the approach. So I only test this method, and not all the methods, from example: cython, numpy, python and numba. Numba is the one used with compute_mandelbrot just because it is the fastest.

## Built With

* [Numpy](https://docs.scipy.org/doc/numpy-1.13.0/reference/) - The framework for array creation and math calculation.
* [Matplotlib](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) - The framework used for ploting.
* [Time](https://docs.python.org/3/library/time.html) - Used for calculating the run time.
* [Sys](https://docs.python.org/3/library/sys.html) - reading arguments from user.
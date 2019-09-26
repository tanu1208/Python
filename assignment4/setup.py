# how to run: sudo python3 setup.py install

from distutils.core import setup
import mandelbrot

name='mandelbrot';
mandelCyt='cython/mandelbrot_4';

setup(name='mandelbrot',
	version='0.1',
	description='mandelbrot',
	py_modules=[name],
	scripts=[name + '.py', mandelCyt + '.py'], 
	)
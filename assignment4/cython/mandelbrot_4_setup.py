#!/usr/bin/env python3
#compile with: python3 mandelbrot_4_setup.py build_ext --inplace

from distutils.core import setup;
from Cython.Build import cythonize;
from distutils.extension import Extension


extensions = [
    Extension("mandelbrot_4_cython", ["mandelbrot_4_cython.pyx"])
    ]

setup(
    ext_modules = cythonize(extensions)
)

# setup(
# 	name = "Integration", 
# 	ext_modules = cythonize('*.pyx')
# 	);
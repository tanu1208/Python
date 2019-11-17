#!/usr/bin/env python
import math
import sys

class Complex:


    def __init__(self, real=0.0, imag=0.0):
        self.real = real;
        self.imag = imag;

    def __repr__(self):
        return "("+str(self.real) + "+" + str(self.imag*1j) + ")"

    # Assignment 3.3

    def conjugate(self):
        return Complex(self.real, -self.imag)   

    def modulus(self):
        return math.sqrt((self.real**2)+(self.imag**2))

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag);

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag);

    def __mul__(self, other):
        re = (self.real * other.real) - (self.imag * other.imag);
        im = (self.real * other.imag) + (self.imag * other.real);
        return Complex(re, im);

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag);


    # Assignment 3.4
    def __radd__(self, other):
        return self + other;

    def __rsub__(self, other):
        if isinstance(other, (float,int)):
            other = Complex(other)
        return other - self;

    def __rmul__(self, other):
        return self * other;

    # Optional, possibly useful methods

    # Allows you to write `-a`
    def __neg__(self):
        return Complex(-self.real, -self.imag)

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        return complex(self.real, self.imag)
        #return complex(Complex(self));

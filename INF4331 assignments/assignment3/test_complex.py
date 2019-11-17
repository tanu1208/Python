#!/usr/bin/env python
import sys
import unittest
from complex import Complex

class TestComplex(unittest.TestCase):

	def test_add(self):
		self.assertEqual(Complex(10, 5) + Complex(10, 5), Complex(20, 10))
		self.assertEqual((Complex(10, 5) + Complex(10, 5)), Complex(20,10))
		self.assertEqual((Complex(214, 411) + Complex(31, 22)), Complex(245,433))
		assert Complex(214, 411) + Complex(31, 22) == Complex(245,433)
		assert 3 + Complex(3,1) == Complex(6, 1)
		assert 40 + Complex(31, 22) == Complex(71,22)
		self.assertEqual(Complex(1, 2) + 3, Complex(4,2))
		assert Complex(1,3) + complex(1,3) == Complex(2, 6)
		self.assertEqual(Complex(1,3) + (1+3j), Complex(2, 6))
		self.assertEqual(Complex(2,3) + (2+2j), Complex(4,5))
		assert Complex(2,3) + (2+2j) == Complex(4,5)

	def test_sub(self):
		self.assertEqual(Complex(10, 5).__sub__(Complex(10, 5)), Complex(0, 0))
		self.assertEqual((Complex(10, 5) - Complex(10, 5)), Complex(0, 0))
		self.assertEqual((Complex(103, 55) - Complex(13, 15)), Complex(90, 40))
		self.assertEqual((4 - Complex(13, 15)), Complex(-9, -15))
		assert Complex(2,3) - (2+2j) == Complex(0,1)
		assert 3 - Complex(2, 1) == Complex(1, -1)
		self.assertNotEqual(Complex(3,4) - 2, Complex(10,2))

	def test_mul(self):
		self.assertEqual(Complex(10, 5).__mul__(Complex(10, 5)), Complex(75, 100))
		self.assertEqual((Complex(10, 5) * Complex(10, 5)), Complex(75, 100))
		self.assertEqual((Complex(3, 25) * Complex(10, 5)), Complex(-95, 265))
		self.assertEqual(4 * Complex(10, 5), Complex(40, 20))
		self.assertNotEqual(4*Complex(3,4) - 2, Complex(10,2))
		assert Complex(2,3) * (2+2j) == Complex(-2,10)
		assert 4 * (2+2j) == Complex(8,8)
		assert (4+1j) * 3 == Complex(12,3)

	def test_eq(self):
		self.assertEqual(Complex(1, 1).__eq__(Complex(1, 1)), Complex(1))
		self.assertEqual(Complex(1, 1) == (Complex(1, 1)), Complex(1))
		self.assertEqual(Complex(124, 112), Complex(124, 112))
		self.assertNotEqual((4+1j), Complex(124, 112))

	def test_modulus(self):
		self.assertEqual(Complex(3, 4).modulus(), 5)
		self.assertEqual(Complex(45, 24).modulus(), 51)
		
	def test_conjugate(self):
		self.assertEqual(Complex(1, 3).conjugate(), Complex(1, -3))
		assert Complex(1,3).conjugate() == Complex(1,-3)

if __name__ == '__main__':
	unittest.main()
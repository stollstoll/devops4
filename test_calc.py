# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:37:45 2024

@author: Vinicius Stoll
"""
#test_calc.py

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        # self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(10, 5), 40)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        # self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, 5), 1)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
    
    def test_square(self):
        # self.assertEqual(calc.square(2, 3),8)
        self.assertEqual(calc.square(2, 3),7)
        self.assertEqual(calc.square(3, 3), 27)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
    
    

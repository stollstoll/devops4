# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:33:43 2024

@author: Vinicius Stoll
"""
#calc.py

def add(x, y):
    'Add Function'
    return x + y     #return 'x' plus 'y' value

def subtract(x, y):
    'Subtract Function'
    return x - y     #return 'x' minus 'y' value

def multiply(x, y):
    'Multiply Function'
    return x * y     #return the multiplication of 'x' by 'y'

def divide(x, y):
    'Divide Function'
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y     #return the division of 'x' by 'y'

def square(x, y):
    'square function'
    return square(x, y)     #return 'x' to the power of 'y' 



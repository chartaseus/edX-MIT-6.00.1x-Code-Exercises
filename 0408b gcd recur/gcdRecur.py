# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:10:32 2022

@author: ASUS
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
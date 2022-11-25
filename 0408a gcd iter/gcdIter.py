# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 08:37:08 2022

@author: ASUS
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a <= b:
        guess = a
    else:
        guess = b
    while guess > 1:
        if a % guess == 0 and b % guess == 0:
            break
        guess -= 1
    return guess
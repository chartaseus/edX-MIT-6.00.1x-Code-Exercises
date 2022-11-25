# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:57:45 2022

@author: ASUS
"""

# Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months

balance = 3926
annualInterestRate = 0.2
lowestPayment = 10
solved = False
while not solved:
    newBalance = balance
    for month in range(12):
        newBalance = (newBalance - lowestPayment) + (annualInterestRate/12.0) * (newBalance - lowestPayment)
    if newBalance <= 0:
        solved = True
    else:
        lowestPayment += 10    
        
print('Lowest payment:', lowestPayment)
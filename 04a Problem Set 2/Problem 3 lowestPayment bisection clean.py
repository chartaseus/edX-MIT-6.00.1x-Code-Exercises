# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:10:53 2022

@author: ASUS
"""

balance = 999999
annualInterestRate = 0.18
lowerBound = balance/12
upperBound = (balance * (1 + (annualInterestRate/12))**12)/12
solved = False
while not solved:
    newBalance = balance
    lowestPayment = (lowerBound + upperBound)/2
    for month in range(12): #calculate remaining balance after one year
        newBalance = (newBalance - lowestPayment) + (annualInterestRate/12.0) * (newBalance - lowestPayment)
    if abs(newBalance) <= 0.01: # if remaining balance < 1 cent, stop the while loop
        solved = True
    elif newBalance > 0.01:
        lowerBound = lowestPayment
    else:
        upperBound = lowestPayment
print('Lowest payment:', round(lowestPayment, 2))
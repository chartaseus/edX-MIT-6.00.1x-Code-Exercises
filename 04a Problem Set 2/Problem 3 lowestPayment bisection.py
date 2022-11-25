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
numGuesses = 0
while not solved:
    newBalance = balance
    lowestPayment = (lowerBound + upperBound)/2
    for month in range(12):
        newBalance = (newBalance - lowestPayment) + (annualInterestRate/12.0) * (newBalance - lowestPayment)
    if abs(newBalance) <= 0.01:
        solved = True
    elif newBalance > 0.01:
        lowerBound = lowestPayment
    else:
        upperBound = lowestPayment
    numGuesses += 1
    print(numGuesses, lowerBound, upperBound, lowestPayment, newBalance)
print('Lowest payment:', round(lowestPayment, 2))
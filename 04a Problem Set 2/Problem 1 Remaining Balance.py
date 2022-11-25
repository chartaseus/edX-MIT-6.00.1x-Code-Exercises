# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 08:59:06 2022

@author: ASUS
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


for month in range (12):        # Calculating remaining balance after a year
    balance = (balance - (monthlyPaymentRate * balance)) + (annualInterestRate/12.0) * (balance - (monthlyPaymentRate * balance))

print('Remaining balance:', round(balance, 2))
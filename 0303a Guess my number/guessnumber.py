# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:58:23 2022

@author: ASUS
"""

print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low + high)//2
correct = False

while not correct:
    ans = (low + high)//2
    print('Is your secret number ' + str(ans) + '?')
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if x == 'c':
        correct = True
    elif x == 'h':
        high = ans
    elif x == 'l':
        low = ans
    else:
        print('Invalid answer.')
    
    
print("Game over. Your secret number was: " + str(ans))
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:13:34 2022

@author: ASUS
"""
# this is my initial working attempt, technically runs correctly but redundant and didn't match the grader. Instead of using Boolean as the while condition, i depended on user input, which caused the need for it to be defined outside the while loop.

# on further investigation it didn't match the grader just because it uses end=' '
print("Please think of a number between 0 and 99!")
low = 0
high = 100
ans = (low + high)//2
print('Is your secret number ' + str(ans) + '?')
x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while x != 'c':
    if x == 'h':
        high = ans
    elif x == 'l':
        low = ans
    else:
        print('Invalid answer.')
    ans = (low + high)//2
    print('Is your secret number ' + str(ans) + '?', end=' ')
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
print("Game over. Your secret number was: " + str(ans))
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 09:00:27 2022

@author: ASUS
"""

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5
s = 'azcbobobegghakl'
count = 0
for letter in s:
    if letter == 'a':
        count += 1
    elif letter == 'e':
        count += 1
    elif letter == 'i':
        count += 1
    elif letter == 'o':
        count += 1
    elif letter == 'u':
        count += 1
print('Number of vowels: ' + str(count))

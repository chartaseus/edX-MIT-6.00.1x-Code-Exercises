# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 09:40:37 2022

@author: ASUS
"""

#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'azcbobobegghakl'
i = 0
count = 0
for letter in s:
    sub = s[i:(i+3)]
    if sub == 'bob':
        count += 1
    i += 1
print('Number of times bob occurs is: ' + str(count))

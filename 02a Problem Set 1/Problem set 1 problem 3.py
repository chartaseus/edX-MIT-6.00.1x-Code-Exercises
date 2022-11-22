# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:57:17 2022

@author: ASUS
"""

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = input('String of lowercase characters: ')
longest = ''
index = 0
sub = ''
for i in s:
    if i >= s[index-1]:
        sub += i
    else:
        sub = i
    if len(sub)>len(longest):
        longest = sub
    index +=1
print('Longest substring in alphabetical order is: ' + longest)
    
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 08:03:18 2022

@author: ASUS
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    num = []
    for i in aDict:
        num.append(len(aDict[i]))
    biggest = None
    for key in aDict.keys():
        if len(aDict[key]) == max(num):
            biggest = key
    return biggest

print(biggest(animals))
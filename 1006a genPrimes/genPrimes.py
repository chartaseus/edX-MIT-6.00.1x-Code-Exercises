# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:51:07 2022

@author: ASUS
"""

def genPrimes():
    # create list to collect prime numbers
    primeList = []
    # first prime number: 2. yield and append to list
    p1 = 2
    yield p1
    primeList.append(p1)
    # second prime number: 3. yield and append to list
    p2 = 3
    yield p2
    primeList.append(p2)
    
    while True:
        #generate next prime candidate: odd integers after 3
        p2 += 2
        #test if prime
        isPrime = True
        for p in primeList:
            # if not prime: break this test, don't append number to primeList, and continue testing the next number
            if (p2 % p) == 0:
                isPrime = False
                break
        # if number is prime: yield, append to primeList
        if isPrime:
            yield p2
            primeList.append(p2)
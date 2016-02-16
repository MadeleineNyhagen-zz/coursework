#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def isprime(n):
    if n == 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print(n)

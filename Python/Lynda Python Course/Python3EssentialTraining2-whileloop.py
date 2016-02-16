#!/usr/bin/python3
# whileloop.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

# simple fibonacci series
# the sume of two elements defines the next set

a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
print("Done.")

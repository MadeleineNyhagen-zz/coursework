#!/usr/bin/python3
# forloop.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

# read the lines from the file
fh = open('lines.txt')

for line in fh.readlines():
    print(line, end='')

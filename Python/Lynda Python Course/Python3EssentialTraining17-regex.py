#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line): # to return all lines with either Lenore or Nevermore
            print(line, end='')

    fh = open('raven.txt')

    for line in fh: # to print only the words Lenore and Nevermore
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())

if __name__ == "__main__": main()

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

def mainTwo(): # search and replace
    fh = open('raven.txt')
    for line in fh: # to print text in raven file but sub '###' for every Lenore or Nevermore
        print(re.sub('(Len|Neverm)ore','###', line), end='')

    fh = open('raven.txt')
    for line in fh: # to print only the lines which contain Lenore or Nevermore, but replace those words with '###'
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end='')

def mainThree(): # a more efficient way of searching for Lenore and Nevermore, using a precompiled regular expression
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE) # re.IGNORECASE ignores case, but re.I would do the same
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')

    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###', line), end='') # same search, now with replace (sub) in print statement
    

##if __name__ == "__main__": main()
##if __name__ == "__main__": mainTwo()
if __name__ == "__main__": mainThree()

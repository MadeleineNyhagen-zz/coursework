#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main(): # iterating with for loops
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='')

    print()

    for line in [1, 2, 3, 4, 5]:
        print(line, end='')

    print()

    for line in 'string':
        print(line)

    print()

def mainTwo(): # enumerating iterators
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

    print()

    a = 'this is a string'
    for index, character in enumerate(a):
        if character == 's': print('index {} is an s'.format(index))

if __name__ == "__main__": main()
if __name__ == "__main__": mainTwo()

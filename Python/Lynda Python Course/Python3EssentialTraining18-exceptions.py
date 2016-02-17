#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

# list of python exceptions available at:
# http://docs.python.org/library/exceptions.html

def main(): # error handling
    try:
        fh = open('xlines.txt')
    except IOError as e:
        print('could not open the file:', e)
    else:
        for line in fh: print(line.strip())

    # or could do this:
    try:
        fh = open('lines.txt')
        for line in fh: print(line.strip())
    except:
        print('you did something wrong.')

def mainTwo():
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except IOError as e:
        print('cannot read file:', e)
    except ValueError as e:
        print('bad filename.', e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('filename must end with .txt')

    

# if __name__ == "__main__": main()
if __name__ == "__main__": mainTwo()

#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the functions.py file.")
    for i in range(25): # only prints through 24
        print(i, end = ' ')
    print()

    for i in inclusive_range(0, 25, 1):
        print(i, end = ' ')
    print()

    for i in inclusive_rangeTwo(25):
        print(i, end = ' ')

# a function that will yield an inclusive range:
def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step

def inclusive_rangeTwo(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <=stop:
        yield i # yield will return a generator
        i += step

if __name__ == "__main__": main()

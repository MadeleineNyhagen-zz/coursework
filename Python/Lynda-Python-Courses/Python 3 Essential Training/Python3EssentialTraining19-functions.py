#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# defining functions:

def main():
    testfunc()
    testfuncTwo()
    testfuncThree(42)

def testfunc():
    print('This is a test function')

def testfuncTwo():
    pass # legal content for a function that doesn't do anything -- a placeholder

def testfuncThree(number, another = None, onemore = 75): # here, another and onemore
    # are assigned default values, making it optional for new values to be passed
    # in to the function. number is still required.
    if another is None:
        another = 112
    print('This is a test function', number, another, onemore)

# using lists of arguments:

def mainTwo():
    testfuncFour(1, 2, 3, 42, 43, 45, 46)

def testfuncFour(this, that, other, *args): # *args allows an indeterminate number of arguments
    # to be passed into the function, creates a tuple
    print(this, that, other)
    for n in args: print(n, end=' ')

# using named function arguments:

def mainThree():
    testfuncFive(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)

def testfuncFive(this, that, other, *args, **kwargs):
    # **kwargs allows the user to enter in keyword arguments, creating a dictionary
    for k in kwargs: print(k, kwargs[k])
    for n in args: print(n)
    print('This is a test function',
          this, that, other, args,
          kwargs['one'], kwargs['two'], kwargs['four'])

# returning values from functions:

def mainFour():
    for n in testfuncSix(): print(n, end=' ')

def testfuncSix():
    return range(25)

# if __name__ == "__main__": main()
# if __name__ == "__main__": mainTwo()
# if __name__ == "__main__": mainThree()
if __name__ == "__main__": mainFour()


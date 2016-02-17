#!/usr/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main(): # using if and else conditional statements
    a, b = 1, 1
    if a < b:
        print('this is true')
    else:
        print('it is not true')

    if True: # if True will execute the if part of the statement
        print('this is true')
    else:
        print('it is not true')


    if False: # if False will execute the else part of the statement
        print('this is true')
    else:
        print('this is false')
    print()

def mainTwo(): # setting multiple choices with elif
    v = 'one'
    if v == 'seven':
        print('v is one')
    elif v == 'two':
        print('v is two')
    elif v == 'three':
        print('v is three')
    else:
        print('v is some other thing')

def mainThree():
    


if __name__ == "__main__": main()
if __name__ == "__main__": mainTwo()
if __name__ == "__main__": mainThree()

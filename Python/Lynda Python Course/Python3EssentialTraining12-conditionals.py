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
    print()

def mainThree():
    a, b = 0, 1
    if a < b: # this is a way of doing this
        c = 'this is true'
    else:
        c = 'this is not true'

    d = 'this is true' if a < b else 'this is not true' # this is an easier way

    print(c)
    print(d)



if __name__ == "__main__": main()
if __name__ == "__main__": mainTwo()
if __name__ == "__main__": mainThree()

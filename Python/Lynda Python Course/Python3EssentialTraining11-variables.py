#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the variables.py file.")
    print()

def mainTwo(): # using numbers
    num = 42 # integer
    numTwo = 42.0 # floating point
    numThree = 42 / 9 # division
    numFour = 42 // 9 # integer division
    numFive = round(42 / 9) # division, rounded
    numSix = round(42 / 9, 2) # division rounded to two
    numSeven = 42 % 9 # to get the remainder of 42/9
    numEight = int(42.9) # to get an integer from a float
    numNine = float(42) # to get a float from an int

    print(type(num), num)
    print(type(numTwo), numTwo)
    print(type(numThree), numThree)
    print(type(numFour), numFour)
    print(type(numFive), numFive)
    print(type(numSix), numSix)
    print(type(numSeven), numSeven)
    print(type(numEight), numEight)
    print(type(numNine), numNine)
    print()

def mainThree(): # strings
    a = 'This is a string!'
    b = 'This is a\nstring!' # using \n to start a new line within the string
    c = r'This is a\nstring!' # using r to indicate a raw string
    d = 'silly'
    e = 42
    f = 'This is a {} string {}.'.format(d, e) # to insert a value or values into a string the new right way
    g = 'This is a %s string!' % d # this is the old way of inserting a value into a string
    h = '''\
this is a string
line after line
of text and more
text. ''' # use ''' or """ to indicate a multiline string.
# \ is used to escape the first new line, so it doesn't show up as a blank line in the string.

    print(a)
    print(b)
    print(c)
    print(f)
    print(g)
    print(h)
    print()

def mainFour():
    a = (1, 2, 3) # tuple object is immutable 
    b = [1, 2, 3] # list object is mutable
    b.append(4) # to demonstrate the mutability of the list, we append
    b.insert(0, 5) # and insert numbers
    b.insert(2, 7) # the first number determines where in the list it is being inserted, while
    # the second number is the number to be added.
    c = 'string'
    
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)
    print(type(c), c[2]) # to print a single character from a string
    print(type(c), c[2:4]) # to print a slice from a string. the first number indicates the place
    # where the slice begins, while the second number indicates the end point
    for i in a: # to iterate through a list of numbers
        print(i)
    for i in c: # to iterate through a string
        print(i)
        print()

def mainFive():
    a = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5} # a dictionary object!
    b = dict( # a better way to create a dictionary object
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    b['seven'] = 7 # to add a value to a dictionary

    print(a)
    for k in sorted(a.keys()):
        print(k, a[k])
    print()
    for k in sorted(b.keys()):
        print(k, b[k])
    

if __name__ == "__main__": main()
if __name__ == "__main__": mainTwo()
if __name__ == "__main__": mainThree()
if __name__ == "__main__": mainFour()
if __name__ == "__main__": mainFive()

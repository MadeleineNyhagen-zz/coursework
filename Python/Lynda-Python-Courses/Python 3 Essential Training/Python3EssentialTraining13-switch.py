#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth',
    )
    v = 'three'
    print(choices[v]) # this will throw an error if v isn't in the dictionary
    z = 'nine'
    print(choices.get(z, 'other')) # this catches that error and returns
    # something of our choice, in this case 'other'
    

if __name__ == "__main__": main()

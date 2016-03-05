#!/usr/bin/python3
# break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    for c in s:
        if c== 's': continue # skips the 's'
        print(c, end='')

    print()

    for c in s:
        if c== 's': break # stops at first 's'
        print(c, end='')

    print()

    for c in s:
        print(c, end='')
    else:
        print('else') # to print 'else' once 'for' action is complete/false

    print()

    i=0
    while(i < len(s)):
        print(s[i], end='')
        i += 1
    else:
        print()
        print('else')

if __name__ == "__main__": main()

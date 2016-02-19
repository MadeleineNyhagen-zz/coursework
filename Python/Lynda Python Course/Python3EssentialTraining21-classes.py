#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, value):
        self._v = value
        print('A duck is born.')
        
    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(47)
    donald.quack()
    donald.walk()
    howard = Duck(131)
    howard.quack()
    howard.walk()
    

if __name__ == "__main__": main()

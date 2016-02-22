#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, value = '1'):
        self._v = value
        print('A duck is born.')
        
    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

class DuckTwo:
    def __init__(self, color = 'white'):
        self._color = color
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color
    

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
    howard = Duck(131)
    howard.quack()
    howard.walk()
    
    daffy = DuckTwo()
    print(daffy.get_color())
    print()
    daffy.set_color('black')
    print(daffy.get_color())

    

if __name__ == "__main__": main()

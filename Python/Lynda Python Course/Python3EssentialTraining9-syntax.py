#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the syntax.py file.")

def mainTwo(): # assigning values
    a = (1, 2, 3, 4, 5)
    b = [1, 2, 3, 4, 5]
    c, d = 0, 1
    c, d = d, c
    print(a)
    print(b)
    print(c, d)
    

def mainThree(): # conditionals
    a, b = 2, 1
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

def mainFour(): # conditionals
    a, b = 1, 1
    s = "less than" if a < b else "not less than"
    print(s)
    
def mainFive(): # functions
    func(1)
    func()
    func(5)
    
def func(a=7): # functions
    for i in range(a, 10):
        print(i, end=' ')
    print()

class Egg: # creating using objects
    def __init__(self, kind = "fried"):
        self.kind = kind

    def whatKind(self):
        return self.kind
        

def mainSix(): # creating using objects
    fried = Egg()
    scrambled = Egg('scrambled')
    print(fried.whatKind(), scrambled.whatKind())


if __name__ == "__main__": main()
if __name__ == "__main__": mainTwo()
if __name__ == "__main__": mainThree()
if __name__ == "__main__": mainFour()
if __name__ == "__main__": mainFive()
if __name__ == "__main__": mainSix()

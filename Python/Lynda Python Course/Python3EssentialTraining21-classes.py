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

class DuckTwo: #using object data: accessor methods

##    def __init__(self, color = 'white'):
##        self._color = color
##        print('Another kind of duck is born.')

    def __init__(self, **kwargs):
        
        # self._color = kwargs.get('color','white')
        self.variables = kwargs
    
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

##    def set_color(self, color): # one way to set/get the object's color
##        self._color = color
##
##    def get_color(self):
##        return self._color

##    def set_color(self, color): # another way to do this
##        self.variables['color'] = color
##
##    def get_color(self):
##        return self.variables.get('color', None)

    def set_variable(self, k, v): # a better way to do this (predicated on using a dictionary,
        # see above self.variables
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)
    

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    print()
    
    daffy = Duck(131)
    daffy.quack()
    daffy.walk()
    print()
    
##    howard = DuckTwo()
##    print(howard.get_color())
##    howard.set_color('black')
    howard = DuckTwo(color = 'blue')
##    print(howard.get_color())
    howard.set_variable('feet', '2')
    print(howard.get_variable('color'))
    print(howard.get_variable('feet'))


    

if __name__ == "__main__": main()

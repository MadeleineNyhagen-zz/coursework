#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

##class Duck:
##    def __init__(self, value = '1'):
##        self._v = value
##        print('A duck is born.')
##        
##    def quack(self):
##        print('Quaaack!', self._v)
##
##    def walk(self):
##        print('Walks like a duck.', self._v)
##
##class DuckTwo: #using object data: accessor methods

##    def __init__(self, color = 'white'):
##        self._color = color
##        print('Another kind of duck is born.')
##
##    def __init__(self, **kwargs):
##        
##        # self._color = kwargs.get('color','white')
##        self.variables = kwargs
##    
##    def quack(self):
##        print('Quaaack!')
##
##    def walk(self):
##        print('Walks like a duck.')

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
##
##    def set_variable(self, k, v): # a better way to do this (predicated on using a dictionary,
##        # see above self.variables
##        self.variables[k] = v
##
##    def get_variable(self, k):
##        return self.variables.get(k, None)
    

##def main():
##    donald = Duck()
##    donald.quack()
##    donald.walk()
##    print()
##    
##    daffy = Duck(131)
##    daffy.quack()
##    daffy.walk()
##    print()

    
##    howard = DuckTwo()
##    print(howard.get_color())
##    howard.set_color('black')
##    howard = DuckTwo(color = 'blue')
####    print(howard.get_color())
##    howard.set_variable('feet', '2')
##    print(howard.get_variable('color'))
##    print(howard.get_variable('feet'))


##class Animal:
##    def talk(self): print('I have something to say!')
##    def walk(self): print('Hey! I''m walkin'' here!')
##    def clothes(self): print('I have nice clothes.')
##
##    
##class DuckThree(Animal):
##            
##    def quack(self):
##        print('Quaaack!')
##
##    def walk(self): # overides the function of the same name in the parent class
##        super().walk() # to access the function walk from the parent class
##        print('Walks like a duck.')
##
##class Dog(Animal):
##    def clothes(self):
##        print('I have brown and white fur.')
##
##def mainTwo():
##    donald = DuckThree()
##    donald.talk()
##    donald.quack()
##    donald.walk()
##
##    fido = Dog()
##    fido.walk()
##    fido.clothes()


# using polymorphism, duck typing
class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('The duck cannot bark.')

    def fur(self):
        print('The duck has feathers.')



class Dog:
    def bark(self):
        print('woof!')

    def fur(self):
        print('The dog has brown and white fur.')

    def walk(self):
        print('Walks like a dog.')

    def quack(self):
        print('The dog cannot quack.')
    
def main():
    donald = Duck()
    donald.quack()
    donald.walk()

    fido = Dog()
    fido.bark()
    fido.fur()

    print()

    for o in (donald, fido): # this works, because each object has functions by these names
        o.quack()
        o.walk()
        o.bark()
        o.fur()
# any object of any class that implements the interface that's expected by any function can be used by that function
    print()

    in_the_forest(donald)
    in_the_pond(fido)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()




if __name__ == "__main__": main()
#if __name__ == "__main__": mainTwo()

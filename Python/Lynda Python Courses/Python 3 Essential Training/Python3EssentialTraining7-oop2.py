#!/usr/bin/python3
# oop2.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaaack!",
        feathers = "The duck has grey and white feathers.",
        bark = "The duck cannot bark.",
        fur = "The duck has no fur."
    )

class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck.",
        feathers = "The person picks a feather from the ground and admires it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack.",
        feathers = "The dog has no feathers.",
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )

def in_the_doghouse(Dog):
    print(Dog.bark())
    print(Dog.fur())

def in_the_forest(Duck):
    print(Duck.quack())
    print(Duck.feathers())

def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest:")
    for o in ( donald, john, fido ):
        in_the_forest(o)

    print("- In the doghouse:")
    for o in ( donald, john, fido ):
        in_the_doghouse(o)

if __name__ == "__main__": main()
    

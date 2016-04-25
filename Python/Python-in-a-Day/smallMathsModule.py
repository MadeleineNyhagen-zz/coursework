# import the function randint from the random module
from random import randint

def multiplyBy5(x):
    return 5 * x

def add5(x):
    return x + 5

def randomAdd(x):
    # get a random integer between 0 and 10
    y = randint(0,10)
    return x + y


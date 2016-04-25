someValue = 5

def letsAdd(x,y):
    addition = x + y
    return addition

print letsAdd(3,5)
print someValue

# make function called subtraction
def subtraction(x,y):
    # make subtract variable equal to x - y
    subtract = x - y
    return subtract

print subtraction(10,4)

# make function that subtracts three variables
def moreSubtraction(x,y,z):
    subtract = x - y - z
    return subtract

print moreSubtraction(40,3,11)

# make function that multiplies two variables
def multiplication(x,y):
    multiply = x * y
    return multiply

print multiplication(5,12)

# make function that divides two variables
def division(x,y):
    # to divide x by y and return a floating point number
    divide = float(x)/float(y)
    return divide

print division(12,4)

# using the len() function
length = len("How epic are built-in functions, huh?")
print length

# using the str() function
x = 23
print "x is equal to: " + str(x)

# using the float() function
y = float(40)/float(7)
print y

# convert a float to an int
yInt = int(y)
print yInt

# if we want to round a float to the nearest whole number
print round(y)

# to round and then convert to an int
print int(round(y))

#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')
    
    print('This is a tuple:')
    t = tuple(range(25))
    print(t)
    print(type(t))
    print(10 in t)
    print(50 in t)
    print(50 not in t)
    print(t[10])
    print(len(t))
    # for i in t: print(i)

    print('This is a list:')
    x = list(range(20))
    print(x)
    print(10 in x)
    print(20 in x)
    # for i in x: print(i)

    # t[10] = 25 will throw an error because tuples are immutable
    x[10] = 25 # is acceptable because lists are mutable
    print(x[10])

    print(t.count(5))
    print(t.index(5))
    # t.append(100) will not work, again because tuples are immutable
    x.append(100) # will work because lists are mutable
    print(x[-1]) # print last number in x to demonstrate that 100 has been appended to x
    print(len(x))
    x.extend(range(20))
    print(x)
    x.insert(0,25)
    print(x)
    x.insert(12,100)
    print(x)    
    x.remove(12) # removes the first instance of the number 12 from x
    print(x)
    del x[12] # removes item at index 12 from x
    print(x)
    print(x.pop()) # returns and removes last item in x
    print(x)
    print(x.pop(0)) # pops first item in x
    print(x)

if __name__ == "__main__": main()

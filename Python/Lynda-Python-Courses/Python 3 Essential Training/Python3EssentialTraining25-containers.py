#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')
##
##    # from the first video on containers:
##    
##    # tuples are immutable, lists are mutable
##    # tuples are created using the comma operator, not by the enclosing parentheses; the parentheses are for binding
##    # t = (1) creates an integer object, not a tuple. to create a tuple with a single element, use t = (1,)
##    t = (1, 2, 3, 4, 5) # a tuple
##    print(t[0]) # to print the first item in the tuple
##    print(t[4]) # to print the fifth item in the tuple
##    print(t[-1]) # to print the last item in the tuple
##    print(len(t)) # to print the length of the tuple
##    print(min(t)) # to print the smallest element of the tuple
##    print(max(t)) # to print the largest element of the tuple
##    t2 = (1) # an integer, not a tuple
##    print(type(t2))
##    t3 = (1,) # a tuple
##    print(type(t3))
##    # lists are created using brackets
##    x = [1, 2, 3, 4, 5] # a list
##    print(type(x))
##    print(x[0])
##
##    # from the second video on containers:
##    
##    print('This is a tuple:')
##    t4 = tuple(range(25))
##    print(t4)
##    print(type(t4))
##    print(10 in t4)
##    print(50 in t4)
##    print(50 not in t4)
##    print(t4[10])
##    print(len(t4))
##    # for i in t4: print(i)
##
##    print('This is a list:')
##    x2 = list(range(20))
##    print(x2)
##    print(10 in x2)
##    print(20 in x)
##    # for i in x2: print(i)
##
##    # t4[10] = 25 will throw an error because tuples are immutable
##    x2[10] = 25 # is acceptable because lists are mutable
##    print(x2[10])
##
##    print(t4.count(5))
##    print(t4.index(5))
##    # t4.append(100) will not work, again because tuples are immutable
##    x2.append(100) # will work because lists are mutable
##    print(x2[-1]) # print last number in x2 to demonstrate that 100 has been appended to x2
##    print(len(x2))
##    x2.extend(range(20))
##    print(x2)
##    x2.insert(0,25)
##    print(x2)
##    x2.insert(12,100)
##    print(x2)    
##    x2.remove(12) # removes the first instance of the number 12 from x2
##    print(x2)
##    del x2[12] # removes item at index 12 from x2
##    print(x2)
##    print(x2.pop()) # returns and removes last item in x2
##    print(x2)
##    print(x2.pop(0)) # pops first item in x2
##    print(x2)

##    # from the third video on containers:
##
##    d = {'one': 1, 'two': 2, 'three': 3} # creates a dictionary
##    print(d)
##
##    d2 = dict(one = 1, two = 2, three = 3) # this does the exact same as above, but is easier to type
##    print(d2)
##    print(type(d), type(d2))
##
##    d3 = dict(four = 4, five = 5, six = 6)
##    print(d3)
##
##    d4 = dict(one = 1, two = 2, three = 3, **d3)
##    print(d4)
##
##    print('four' in d3)
##    print('three' in d3)
##
##    for k in d4: print(k)
##    for k, v in d4.items(): print(k, v)
##
##    print(d4['three']) # returns the value associated with the 'three' key
##    # print(d3['three']) will raise an exception, because d3 doesn't have a 'three'
##    print(d3.get('three')) # will instead return 'None' if there is no match
##    print(d4.get('three')) # returns the value associated with 'three'
##    print(d3.get('three', 'not found')) # returns 'not found' instead of 'None' if 'three' isn't found in the dictionary
##
##    del d3['four'] # deletes 'four' and its associated value from the dictionary
##    print(d3)
##    print(d3.pop('five')) # pops 'five' and its associated value from the dictionary
##    print(d3)

    # from the fourth video on containers

    # reading a utf-8 file using a byte array

    fin = open('utf8.txt', 'r', encoding = 'utf_8')
    fout = open('utf8.html', 'w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127: # because there are 128 (0-127) values in utf-8 that are normal ascii characters
                # if the character is outside of the normal ascii range, we encode it with an xml entity (passed into 'bytes()'),
                # which can be used in an html context
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            else: outbytes.append(ord(c)) # if the character is within the normal ascii range, it is appended to outbytes
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr, file = fout)
    print(outstr)
    print('Done.')

    

if __name__ == "__main__": main()

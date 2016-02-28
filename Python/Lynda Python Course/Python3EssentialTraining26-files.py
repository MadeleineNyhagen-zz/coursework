#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # from the first video on files:

    # to read a file:
    
##    f = open('lines.txt')
##    for line in f:
##        print(line, end = '')

    # from the second video on files:
    
    # to copy the contents of a file to a new file:

##    infile = open('lines.txt', 'r')
##    outfile = open('new.txt', 'w')
##    for line in infile:
##        print(line, file = outfile, end = '')
##    print('Done.')

    # reading/writing a large file:

##    buffersize = 50000
##    infile = open('bigfile.txt', 'r')
##    outfile = open('new.txt', 'w')
##    buffer = infile.read(buffersize) # the read method isn't iterable, so we will have to use
##    # a while loop instead of a for loop:
##    while len(buffer):
##        outfile.write(buffer)
##        print('.', end = '')
##        buffer = infile.read(buffersize)
##    print()
##    print('Done.')

    # from the third video on files:

    #reading/writing a binary file, must be done using buffered I/O:
    
    buffersize = 50000
    infile = open('olives.jpg', 'rb') # the 'rb' puts it in read binary mode
    outfile = open('new.jpg', 'wb') # 'wb' puts it in write binary mode
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print()
    print('Done.')


if __name__ == "__main__": main()

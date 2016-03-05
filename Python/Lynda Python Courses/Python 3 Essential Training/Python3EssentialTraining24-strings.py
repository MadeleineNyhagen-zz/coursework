#!/usr/bin/python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())

    s1 = 'this is a string\n'
    print(s1)
    print(s1.rstrip()) # can specify a string to be stripped

    a, b = 5, 42
    print('this is {}, that is {}'.format(a, b))
    print('this is {0}, that is {1}, this is also {1}, and that is {0}'.format(a,b))
    print('this is {bob} and that is {fred}'.format(bob = a, fred = b))
    s2 = 'this is {}, that is {}'
    print(s2.format(a,b))

    d = dict( bob = a, fred = b )
    'this is {bob}, this is {fred}'.format(**d)

    s3 = 'This is a string of words'
    print(s3)
    print(s3.split())
    print(s3.split('i'))
    words = s3.split()
    print(words)
    for w in words: print(w)
    new = ':'.join(words)
    print(new)
    new2 = s3.center(80)
    print(new2)

    # to learn more about string methods, go to http://docs.python.org/py3k/library/stdtypes.html#string-methods

if __name__ == "__main__": main()

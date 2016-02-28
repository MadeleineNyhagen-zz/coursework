#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# find documentation on python modules here:
# http://docs.python.org/py3k/library/index.html under the python runtime services heading

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

##    # the os module
##    import os
##    print(os.name)
##    print(os.getenv('PATH'))
##    print(os.getcwd())
##    print(os.urandom(25))

##    # the urllib module
##    import urllib.request
##    page = urllib.request.urlopen('http://bw.org/')
##    print(page)
##    for line in page: print(str(line, encoding = 'utf_8'), end = '')

##    # the random module
##    import random
##    print(random.randint(1,1000))
##    print(random.randint(1,1000))
##    print(random.randint(1,1000))
##    x = list(range(25))
##    print(x)
##    random.shuffle(x)
##    print(x)
##    random.shuffle(x)
##    print(x)
##    random.shuffle(x)
##    print(x)

    # the datetime module
    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == "__main__": main()

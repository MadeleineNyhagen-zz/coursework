#!/usr/bin/python3
# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

def main():
    print('This is the databases.py file')

    db = sqlite3.connect('test.db') # connect to or create the database
    db.row_factory = sqlite3.Row # row_factory allows us to determine how rows are returned from the cursor
    db.execute('drop table if exists test') # drop table if exists
    db.execute('create table test (t1 text, i1 int)') # create table
    # populate table:
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    # commit changes:
    db.commit()
    # display data from table:
    cursor = db.execute('select * from test order by t1')

    # use without row factory to return table contents as tuples:
    for row in cursor:
        print(row)

    # use with row factory to return table contents as a dictionary:
    cursor = db.execute('select * from test order by i1')
    for row in cursor:
        print(dict(row))

    cursor = db.execute('select * from test order by i1')
    for row in cursor:
        print(row['t1'], row['i1'])

    # documentation for row_factory can be found on the sqlite3 page of the python documentation:
    # http://docs.python.org/py3k/library/sqlite3.html

if __name__ == "__main__": main()

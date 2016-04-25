import sqlite3

# connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

### create table named SIMPSON_INFO
##conn.execute("CREATE TABLE SIMPSON_INFO ( \
##    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
##    NAME TEXT, \
##    GENDER TEXT, \
##    AGE INT, \
##    OCCUPATION TEXT );")

### add Bart Simpson to table
##conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION)\
##             VALUES ('Bart Simpson', 'Male', 10, 'Student');")
##
### add Homer Simpson to table
##conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION)\
##             VALUES ('Homer Simpson', 'Male', 40, 'Nuclear Plant');")
##
### add Lisa Simpson to table
##conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION)\
##             VALUES ('Lisa Simpson', 'Female', 8, 'Student');")
##
### save changes
##conn.commit()
##
### print number of changes to database
##changes = conn.total_changes
##print "Number of changes: ", changes

### get data from database
##cursor = conn.execute("SELECT * from SIMPSON_INFO")
##print cursor
##
### get data from cursor
##rows = cursor.fetchall()
##print rows

### print homer's row from database
##hcursor = conn.execute("SELECT * FROM SIMPSON_INFO WHERE NAME='Homer Simpson'")
##hrow = hcursor.fetchall()
##print hrow
##
# print female characters' rows from database
##fcursor = conn.execute("SELECT * FROM SIMPSON_INFO WHERE GENDER='Female'")
##frow = fcursor.fetchall()
##print frow
##
### print student characters' rows from database
##scursor = conn.execute("SELECT * FROM SIMPSON_INFO WHERE OCCUPATION='Student'")
##srow = scursor.fetchall()
##print srow

##conn.execute("DELETE FROM SIMPSON_INFO WHERE ID=2;")
##conn.commit()
##
### print number of changes to database
##changes = conn.total_changes
##print "Number of changes: ", changes
##
### print data from database
##cursor = conn.execute("SELECT * FROM SIMPSON_INFO")
##rows = cursor.fetchall()
##print rows

### update Bart's age
##conn.execute("UPDATE SIMPSON_INFO SET AGE=11 WHERE NAME='Bart Simpson';")
##conn.commit()
##
### print number of changes to database
##changes = conn.total_changes
##print "Number of changes: ", changes
##
### print data from database
##cursor = conn.execute("SELECT * FROM SIMPSON_INFO")
##rows = cursor.fetchall()
##print rows

### drop the table
##conn.execute("DROP TABLE SIMPSON_INFO")

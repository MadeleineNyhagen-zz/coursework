import sqlite3
from datetime import datetime
import calendar

# connect to timestamp database
conn = sqlite3.connect('timestamp.db')

def createTable():
    conn.execute("CREATE TABLE if not exists \
        Time_Stamps(Time_Checked INTEGER);")

def addTimeStamp():
    d = datetime.utcnow()
    timestamp = calendar.timegm(d.utctimetuple())
    inserttime = "INSERT INTO Time_Stamps \
        (Time_Checked) VALUES ({})".format(timestamp)
    #print timestamp
    #print inserttime
    conn.execute(inserttime)
    conn.commit()

# to return the time 

def lastChecked():
    lastcheck = conn.execute("SELECT MAX(Time_Checked) FROM Time_Stamps")
    for row in lastcheck:
        timestamp = datetime.fromtimestamp(row[0])
##        print(timestamp)
##        print(row[0])
        return "Last file check: {}".format(timestamp)

def viewTable():
    vt = conn.execute("SELECT * FROM Time_Stamps")
    for row in vt:
        print(row)
    print(vt)

    
#addTimeStamp()
#lastChecked()
#viewTable()

##d = datetime.utcnow()
##timestamp = calendar.timegm(d.utctimetuple())
##ft = datetime.fromtimestamp(timestamp)
##print(d)
##print(timestamp)
##print(ft)

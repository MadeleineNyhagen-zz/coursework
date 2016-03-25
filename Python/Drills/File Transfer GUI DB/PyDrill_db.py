import sqlite3

# connect to timestamp database
conn = sqlite3.connect('timestamp.db')

def createTable():
    conn.execute("CREATE TABLE if not exists \
        Time_Stamps(Time_Checked INTEGER);")

def lastChecked():
    lastCheck = conn.execute("SELECT MAX(Time_Checked) FROM Time_Stamps)
        print "Date of last file check was: ",

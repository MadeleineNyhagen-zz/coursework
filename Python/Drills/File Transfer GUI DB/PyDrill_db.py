import sqlite3

# connect to timestamp database
conn = sqlite3.connect('timestamp.db')

def createTable():
    conn.execute("CREATE TABLE if not exists \
        Time_Stamps(Time_Checked INTEGER);")

def lastChecked():
    lastCheck = conn.execute("SELECT MAX(Time_Checked) FROM Time_Stamps")
    return "Date of last file check was: {}".format(lastCheck)

def addTimeStamp(dt):
    insertTime = "INSERT INTO Time_Stamps \
        (Time_Checked) VALUES ({})".format(dt)
    print insertTime
    conn.execute(insertTime)
    conn.commit

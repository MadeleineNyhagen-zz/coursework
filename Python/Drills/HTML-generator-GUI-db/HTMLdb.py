import sqlite3

db = sqlite3.connect('htmlpage.db')
cursor = db.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS \
            bodytext( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            Name TEXT, \
            Content TEXT \
            );")
    db.commit()

createTable()

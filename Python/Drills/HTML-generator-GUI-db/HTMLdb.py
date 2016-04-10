import sqlite3

db = sqlite3.connect('htmlpage.db')
cursor = db.cursor()

##cursor.execute("DROP TABLE bodytext")
##db.commit()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS \
            bodytext( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            Title TEXT, \
            Content TEXT \
            );")
    db.commit()

createTable()

def newPage(title, content):
    addvalues = "'{}', '{}'".format(title, content)
    addpage = "INSERT INTO bodytext (Title, Content) VALUES \
        ({});".format(addvalues)
    cursor.execute(addpage)
    db.commit()
    return db.total_changes

# newPage('test', 'this is the body')

def displayAll():
    select = "SELECT * FROM bodytext"
    display = cursor.execute(select)
    rows = display.fetchall()
    return rows

for item in displayAll():
    print(item)
    

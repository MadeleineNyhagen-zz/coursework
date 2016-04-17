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

def displayItem(title):
    select = "SELECT Content FROM bodytext WHERE Title = '{}';".format(title)
    #select = "SELECT Content FROM bodytext WHERE Title = 'test';"
    #select = "SELECT Content FROM bodytext;"
    display = cursor.execute(select)
    rows = display.fetchall()
    return rows
    print(rows)


def displayAll():
    select = "SELECT * FROM bodytext;"
    display = cursor.execute(select)
    rows = display.fetchall()
    return rows

##for item in displayAll():
##    print(item)
    
#displayItem(title)

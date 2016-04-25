import sqlite3
import time
import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect('tutorial.db') # connect to database
c = conn.cursor() # specify cursor
wordUsed = 'Python Sentiment'
sql = "SELECT * FROM stuffToPlot WHERE keyword = ?"

graphArray = []

for row in c.execute(sql, [(wordUsed)]):
    startingInfo = str(row).replace(')', '').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[2]+','+splitInfo[4]
    graphArray.append(graphArrayAppend)
##    print(graphArrayAppend)
##    time.sleep(3)

datestamp, value = np.loadtxt(graphArray, delimiter=',', unpack=True, 
                              converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})

fig = plt.figure()

rect = fig.patch

ax1 = fig.add_subplot(1,1,1, axisbg='white')
plt.plot_date(x = datestamp, y = value, fmt='b-', label = 'value', linewidth=2)
plt.show()



##def tableCreate():
##    c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
##
##idfordb = 4
##keyword = 'Python Sentiment'
##value = 7
##    
##def dataEntry():
##    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
##    c.execute("INSERT INTO stuffToPlot(ID, unix, datestamp, keyword, value) VALUES (?,?,?,?,?)",
##              (idfordb, time.time(), date, keyword, value))
##    conn.commit()
##
##
##def readData():
##    for row in c.execute(sql,[(wordUsed)]):
##        print(str(row).replace(')', '').replace('(','').replace('u\'','').replace("'",""))

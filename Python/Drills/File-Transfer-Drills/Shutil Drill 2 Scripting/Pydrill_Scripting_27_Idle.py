import os
import shutil
import datetime
from datetime import datetime,timedelta

source='C:/Users/stud/Desktop/A'
destination='C:/Users/stud/Desktop/B'

#call last modification time of file and return a readable timestamp:

def modDate(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t)

#call creation time of file and return a readable timestamp:

def createDate(filename):
    t = os.path.getctime(filename)
    return datetime.fromtimestamp(t)



#to compare the file timestamps to the current time and determine whether they've been modified in the last 24 hours:

now = datetime.now()

def compDates(filenames):
    recentMod = now - modDate(filenames)
    recentCreate = now - createDate(filenames)
    if recentMod < timedelta(hours=24) or recentCreate < timedelta(hours=24):
        return True
    else:
        return False



#to move files if they have been modified or created in the last 24 hours:

for files in os.listdir(source):
    path = source + "/" + files
    if compDates(path):
        shutil.move(path, destination)
        print (path + " moved to " + destination + "/" + files)






# to move a folder:
# shutil.copytree('C:/Users/stud/Desktop/A','C:/Users/stud/Desktop/B/A')
# to delete a folder:
# shutil.rmtree('C:/Users/stud/Desktop/B/A')
# to move a file:
# shutil.copy('C:/Users/stud/Desktop/A/C.txt','C:/Users/stud/Desktop/B')
# to delete a file:
# os.remove('C:/Users/stud/Desktop/B/C.txt')
# to move a folder:
# shutil.move('C:/Users/stud/Desktop/A','C:/Users/stud/Desktop/B')
# I think to copy permissions:
# shutil.copymode('C:/Users/stud/Desktop','C:/Users/stud/Desktop/B')

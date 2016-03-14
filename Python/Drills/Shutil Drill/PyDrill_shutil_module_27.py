import os
import shutil

source = 'C:/Users/stud/Desktop/A'
destination = 'C:/Users/stud/Desktop/B'

for files in os.listdir(source):
    path = source + "/" + files
    shutil.move(path, destination)
    print(destination + "/" + files)



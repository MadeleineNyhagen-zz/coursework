import os, csv

# the path to the script
currentPath = os.path.dirname(os.path.abspath("__file__"))

# make the spreadsheet path
inputCsv = currentPath + '\spreadsheet.csv'
print inputCsv

# open file in read mode
csvFile = open(inputCsv, "rb")

# create reader object
reader = csv.reader(csvFile, delimiter=',')


readerData = []

# print out data in file
# add data to array
for row in reader:
    readerData.append(row)

print readerData

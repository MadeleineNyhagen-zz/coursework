import os, csv
# the path to the script
currentPath = os.path.dirname(os.path.abspath("__file__"))
print currentPath

# make the spreadsheet path
outputCsv = currentPath + '\spreadsheet.csv'
print outputCsv

# open the file
csvFile = open(outputCsv, "wb")

# create writer object
writer = csv.writer(csvFile, delimiter=',')

# data to go in csv
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

# # write rows to csv
# writer.writerow(row_1)
# writer.writerow(row_2)
# writer.writerow(row_3)

# all rows
rows = [row_1, row_2, row_3]

# loop rows and write each
for row in rows:
    writer.writerow(row)
csvFile.close()

import csv
import re
import os
import numbers
import decimal

files = ["companylist1.csv","companylist2.csv","companylist3.csv"]
symbols=[]
names=[]
def __init__():
    main()
def readIntoRows(nameofcsv):
    global symbols
    global names
    with open(nameofcsv) as csvfile:
        filereader = csv.reader(csvfile, delimiter =',')
        first = True
        for row in filereader:
            if(first):
                first=False
                continue
            symbols.append(row[0])
            names.append(row[1])
        symbols = sorted(symbols)
        names = sorted(names)


def main():
    for file in files:
        readIntoRows(file)
main()
#Realistic Name Generator by Mike Bradley
#Based on 2000 US Census and Social Security Data

import sys
import os
import csv
import random

__location__ = os.path.dirname(os.path.abspath(sys.argv[0]))



f = open(os.path.join(__location__, 'FemaleNames.csv'),'rU')
reader = csv.reader(f)
fNames = []
for line in reader:
	fNames.append(line)
f.close()

f = open(os.path.join(__location__, 'MaleNames.csv'),'rU')
reader = csv.reader(f)
mNames = []
for line in reader:
	mNames.append(line)
f.close()

f = open(os.path.join(__location__, 'LastNames.csv'),'rU')
reader = csv.reader(f)
lNames = []
for line in reader:
	lNames.append(line)
f.close()

total = 0
for item in fNames:
        total += int(item[1])
        item[1] = total

total = 0
for item in mNames:
        total += int(item[1])
        item[1] = total
        
total = 0
for item in lNames:
        total += int(item[1])
        item[1] = total

def NameFunc(gender):

    if gender == "M" or gender == "m":
            first = random.randint(0,int(mNames[int(len(mNames))-1][1]))
            last = random.randint(0,int(lNames[int(len(lNames))-1][1]))
            mName = mNames[0][0]
            lName = lNames[0][0]
            for x in range(len(mNames)):
                    if int(mNames[x][1])<= first:
                            mName = mNames[x][0]
            for x in range(len(lNames)):
                    if int(lNames[x][1])<= last:
                            lName = lNames[x][0]

            return(mName+" "+lName)

    elif gender == "F" or gender == "f":
            first = random.randint(0,int(fNames[int(len(fNames))-1][1]))
            last = random.randint(0,int(lNames[int(len(lNames))-1][1]))
            fName = fNames[0][0]
            lName = lNames[0][0]
            for x in range(len(fNames)):
                    if int(fNames[x][1])<= first:
                            fName = fNames[x][0]
            for x in range(len(lNames)):
                    if int(lNames[x][1])<= last:
                            lName = lNames[x][0]

            return(fName+" "+lName)

    else:
        return("Invalid Gender")

#Hometown Generator by Mike Bradley

import sys
import os
import csv
import random

__location__ = os.path.dirname(os.path.abspath(sys.argv[0]))



f = open(os.path.join(__location__, 'Towns.csv'),'rU')
reader = csv.reader(f)
towns = []
for line in reader:
	towns.append(line)
f.close()


total = 0
for item in towns:
        item.append(item[1])
        total += int(item[1])
        item[1] = total


def TownFunc():


	
	townNum = random.randint(0,int(towns[int(len(towns))-1][1]))

	town = towns[0][0]
	state = towns[0][2]
	for x in range(len(towns)):
			if int(towns[x][1])<= townNum:
					town = towns[x][0]
					state = towns[x][2]
					population = towns[x][3]

	

	
	reString = town + ", " + state + "; Population:" + population

	return(reString)

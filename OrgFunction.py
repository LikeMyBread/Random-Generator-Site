#Organization Generator by Mike Bradley

import sys
import os
import csv
import random

__location__ = os.path.dirname(os.path.abspath(sys.argv[0]))



f = open(os.path.join(__location__, 'data/Nouns.csv'),'rU')
reader = csv.reader(f)
nouns = []
for line in reader:
	nouns.append(line)
f.close()

f = open(os.path.join(__location__, 'data/Causes.csv'),'rU')
reader = csv.reader(f)
causes = []
for line in reader:
	causes.append(line)
f.close()

f = open(os.path.join(__location__, 'data/Stances.csv'),'rU')
reader = csv.reader(f)
stances = []
for line in reader:
	stances.append(line)
f.close()

f = open(os.path.join(__location__, 'data/Firsts.csv'),'rU')
reader = csv.reader(f)
firsts = []
for line in reader:
	firsts.append(line)
f.close()

total = 0
for item in nouns:
        total += int(item[1])
        item[1] = total

total = 0
for item in firsts:
        total += int(item[1])
        item[1] = total

total = 0
for item in stances:
        total += int(item[1])
        item[1] = total

total = 0
for item in causes:
        total += int(item[1])
        item[1] = total

def OrgFunc():



	
	nounNum = random.randint(0,int(nouns[int(len(nouns))-1][1]))
	causeNum = random.randint(0,int(causes[int(len(causes))-1][1]))
	stanceNum = random.randint(0,int(stances[int(len(stances))-1][1]))
	firstNum = random.randint(0,int(firsts[int(len(firsts))-1][1]))
	
	noun = nouns[0][0]
	for x in range(len(nouns)):
			if int(nouns[x][1])<= nounNum:
					noun = nouns[x][0]

	cause = causes[0][0]
	for x in range(len(causes)):
			if int(causes[x][1])<= causeNum:
					cause = causes[x][0]

	stance = stances[0][0]
	for x in range(len(stances)):
			if int(stances[x][1])<= stanceNum:
					stance = stances[x][0]
	first = ""
	if random.randint(0,1) == 1:
		first = firsts[0][0]
		for x in range(len(firsts)):
				if int(firsts[x][1])<= firstNum:
						first = firsts[x][0]
		first += " "

	
	reString = first + noun + " " + stance + " " + cause

	return(reString)

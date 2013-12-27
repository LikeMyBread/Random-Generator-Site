#Personality Generator by Mike Bradley

import sys
import os
import csv
import random
import Situations
import Responses


situations = []
responses = []

for i in dir(Situations):
    if i[0] != '_':
        situations.append(i)

for i in dir(Responses):
    if i[0] != '_':
        responses.append(i)

def PersFunc(numTraits):
    
    personality = []
    for x in range(numTraits):
        personality.append([random.choice(situations),random.choice(responses),random.randint(0,100)])

    return(personality)


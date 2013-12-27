#Random Generators by Mike Bradley

from flask import Flask
app = Flask(__name__)
app.debug = True #Makes flask automaticaly update every time the file is saved


import NameFunction
import OrgFunction
import TownFunction
import PersonalityFunction
import random

global NameFunction
global OrgFunction
global TownFunction
global PersonalityFunction
global random


@app.route('/')
def startHere(result=""):

    
    html = '''<html>

<head>
<title>Mike's Random Generators</title>
<style type="text/css">
.genButton{background-color: #4fa76a; height: 30px; width: 100px;float:left;margin:0px auto;text-align:center;text-decoration: none;color:black;}
.genButton:hover{background-color:#23663b}
</style>
</head>


<body>

<div id="container" style="width:100%;min-width:500px">

<div id="heading" style="background-color:#4fa76a">
	<h1 style="margin:0px auto;text-align:center">Mike's Random Generators</h1>
</div>

<div id="buttonBar" style="width:100px;float:left">
	
	<a class="genButton" href="/malename">Male Name</a>
	<a class="genButton" href="/femalename">Female Name</a>
	<a class="genButton" href="/hometown">Hometown</a>
	<a class="genButton" href="/organization">Organization</a>
	<a class="genButton" href="/personality">Personality</a>
</div>

<div id="resultsArea" style="width:80%;min-width:100px;float:left">
'''+result+'''
</div>

</div>

</body>
</html>'''

    return(html)

#Generators go down here

@app.route("/malename")
def maleName():
    return(startHere(NameFunction.NameFunc('m')))

@app.route("/femalename")
def femaleName():
    return(startHere(NameFunction.NameFunc('f')))

@app.route("/hometown")
def homeTown():
    return(startHere(TownFunction.TownFunc()))

@app.route("/organization")
def organization():
    return(startHere(OrgFunction.OrgFunc()))

@app.route("/personality")
def organization():
    return(startHere(str(PersonalityFunction.PersFunc(5))))



if __name__ == '__main__': #Starts the website
    app.run()

#Random Generators by Mike Bradley

from flask import Flask
app = Flask(__name__)
app.debug = True #Makes flask automaticaly update every time the file is saved


import NameFunction
import OrgFunction
import TownFunction
import random

global NameFunction
global OrgFunction
global TownFunction
global random


@app.route('/')
def startHere(result=""):
#    mName = NameFunction.NameFunc('m')
#    fName = NameFunction.NameFunc('f')
#    organization = OrgFunction.OrgFunc()
#    town = TownFunction.TownFunc()

    
    html = '''<html>

<head>
<title>Mike's Random Generators</title>
<style type="text/css">
.genButton{background-color: Aquamarine; height: 30px; width: 100px;float:left;margin:0px auto;text-align:center}
</style>
</head>


<body>

<div id="container" style="width:100%;min-width:500px">

<div id="heading" style="background-color:Aquamarine">
	<h1 style="margin:0px auto;text-align:center">Mike's Random Generators</h1>
</div>

<div id="buttonBar" style="width:100px;float:left">
	
	<a href="/malename">
		<div class="genButton">Male Name</div>
	</a>
	<a href="/femalename">
		<div class="genButton">Female Name</div>
	</a>
	<a href="/hometown">
		<div class="genButton">Hometown</div>
	</a>
	<a href="/organization">
		<div class="genButton">Organization</div>
	</a>
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
def maleName():
    return(startHere(TownFunction.TownFunc()))

@app.route("/organization")
def organization():
    return(startHere(TownFunction.TownFunc()))



if __name__ == '__main__': #Starts the website
    app.run()

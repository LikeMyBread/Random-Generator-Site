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
def startHere():
    mName = NameFunction.NameFunc('m')
    fName = NameFunction.NameFunc('f')
    organization = OrgFunction.OrgFunc()
    town = TownFunction.TownFunc()

    
    html = '''<div style="width: 500px; height: 300px; margin:auto;text-align:center">Mike's Generators</div>'''+'Male Name: '+ mName +'<div/>'+ 'Female Name: '+fName +'<div/>'+'<div/>'+ 'Organization: '+ organization +'<div/>'+'<div/>'+'Town: '+ town
    return(html)










if __name__ == '__main__': #Starts the website
    app.run()

# Callaghan Donnelly
# 8/7/2022
# the functions to actually write the python code for all the graphics objects that have been drawn

import graphics
from graphics import *


def getFormObjects(form):
    # I can ignore items 0-21 as those are the setup items
    # remove all default objects from the list, so only the new items will be added to new form
    modList = form.items
    del modList[0:21]

    return modList


# for each item after [20]
#  create a variable for it
#  adjust its coordinates based on where it is in the usable box on the original form
#  get its fill color if its a polygon or its text color if its a label
#  write it's code and draw to new default form
def handleFormObjects(obList):
    # default code to setup the window
    startupStr = 'import graphics\nfrom graphics import *\n\n# Setup default window for drawing objects\nwin = GraphWin("Form title goes here", 1470, 880)\n\n'

    # default numbers to start each object's code
    recCounter = 0
    circCounter = 0
    lblCounter = 0

    for object in obList:
        # stub names for each objects variable
        recVar = f'rec{recCounter}'
        circVar = f'circ{circCounter}'
        lblVar = f'lbl{lblCounter}'
        # modify the coordinate points so it doesn't come out off kilter in the new form
        object.move(-270, -10)

        if isinstance(object, Rectangle):
            startupStr = startupStr + recVar + ' = ' + str(object) + '\n'
            obColor = object.config['fill']
            startupStr = startupStr + recVar + '.setFill(\'' + str(obColor) + '\')\n'
            startupStr = startupStr + recVar + '.draw(win)\n\n'
            recCounter = recCounter + 1

        elif isinstance(object, Circle):
            startupStr = startupStr + circVar + ' = ' + str(object) + '\n'
            obColor = object.config['fill']
            startupStr = startupStr + circVar + '.setFill(\'' + str(obColor) + '\')\n'
            startupStr = startupStr + circVar + '.draw(win)\n\n'
            circCounter = circCounter + 1

        elif isinstance(object, Text):
            startupStr = startupStr + lblVar + ' = ' + str(object) + '\n'
            obColor = object.config['fill']
            startupStr = startupStr + lblVar + '.setTextColor(\'' + str(obColor) + '\')\n'
            startupStr = startupStr + lblVar + '.draw(win)\n\n'
            lblCounter = lblCounter + 1

        # unmodify the coordinate points so the objects flicker instead of shift totally
        object.move(270, 10)

    return startupStr


# write the python code out to a file
def writeToFile(codeStr):
    with open('graphicCode.py', 'w+') as outFile:
        outFile.write(codeStr)


def writeFormCode(win):
    modifiedList = getFormObjects(win)
    writeStr = handleFormObjects(modifiedList)
    writeToFile(writeStr)

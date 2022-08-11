# Callaghan Donnelly
# making my take on a Visual Studio esque environment for Python using John Zelle's graphics class (as well as its underlying Tkinter base)
# 8/5/2022

import tkinter.ttk
import graphics
from graphics import *
import math
from math import *
import pyWriter
from pyWriter import *

win = GraphWin("Create your window", 1750, 900)

# DO NOT LET THEM TOUCH THIS RECTANGLE
rec = Rectangle(Point(50, 50), Point(250, 490))
rec.setFill('grey')
rec.draw(win)

# draw the usable area
playRec = Rectangle(Point(270, 10), Point(1740, 890))
playRec.draw(win)

# Draw the sample rectangle
selectRect = Rectangle(Point(80, 90), Point(210, 150))
selectRect.setFill('red')
selectRect.draw(win)

# Draw the sample circle
selectCirc = Circle(Point(140, 260), 60)
selectCirc.setFill('red')
selectCirc.draw(win)

# Draw the sample Label
selectLbl = Text(Point(140, 380), "Label")
selectLbl.setTextColor('red')
selectLbl.setSize(26)
selectLbl.draw(win)

# Draw the cursor button
selectUnbind = Text(Point(150, 440), "Regular cursor")
selectUnbind.setSize(20)
selectUnbind.draw(win)

# Draw the Undo button
btnUndo = Rectangle(Point(50, 520), Point(250, 620))
btnUndo.setFill('dark blue')
btnUndo.draw(win)
lblUndo = Text(Point(145, 570), "Undo last item")
lblUndo.setSize(18)
lblUndo.setTextColor('white')
lblUndo.draw(win)

# Draw the color palette
setSqr = Rectangle(Point(50, 645), Point(250, 755))
setSqr.draw(win)
# black option
blkSrq = Rectangle(Point(55, 655), Point(95, 695))
blkSrq.setFill('black')
blkSrq.draw(win)
# red option
redSrq = Rectangle(Point(105, 655), Point(145, 695))
redSrq.setFill('red')
redSrq.draw(win)
# blue option
bluSrq = Rectangle(Point(155, 655), Point(195, 695))
bluSrq.setFill('blue')
bluSrq.draw(win)
# green option
grnSrq = Rectangle(Point(205, 655), Point(245, 695))
grnSrq.setFill('green')
grnSrq.draw(win)
# second column
# white option
whtSrq = Rectangle(Point(55, 705), Point(95, 745))
whtSrq.setFill('white')
whtSrq.draw(win)
# yellow option
ylwSrq = Rectangle(Point(105, 705), Point(145, 745))
ylwSrq.setFill('yellow')
ylwSrq.draw(win)
# orange option
ongSrq = Rectangle(Point(155, 705), Point(195, 745))
ongSrq.setFill('orange')
ongSrq.draw(win)
# purple option
prpSrq = Rectangle(Point(205, 705), Point(245, 745))
prpSrq.setFill('purple')
prpSrq.draw(win)

# Draw the Save button
saveBtn = Rectangle(Point(50, 765), Point(250, 830))
saveBtn.setFill('light blue')
saveBtn.draw(win)
saveLbl = Text(Point(150, 795), 'Save')
saveLbl.setTextColor('white')
saveLbl.setSize(22)
saveLbl.draw(win)

# Draw the Exit button
btnExit = Rectangle(Point(50, 840), Point(250, 895))
btnExit.setFill('black')
btnExit.draw(win)
lblExit = Text(Point(150, 865), "Exit")
lblExit.setSize(22)
lblExit.setTextColor('white')
lblExit.draw(win)

# ------------------------------------TEST AREA FOR FORM OBJECTS----------------------------
# ignore win.items 0-20 as they are the setup objects
# print(win.items[20])

# ------------------------------------------------------------------------------------------


global dragcoordX
global dragcoordY
lastItem = None
chosenColor = None


# TODO: in all the draw events: supress or fix the list.remove() ValueError
# Drawing/redrawing rectangles with a given tinkter event
def drawRec(event):
    global myRectangle
    global lastItem
    global chosenColor
    try:
        myRectangle.undraw()
    except NameError as e:
        pass
    myRectangle = Rectangle(Point(dragcoordX, dragcoordY), Point(event.x, event.y))
    if chosenColor is None:
        chosenColor = 'black'
    myRectangle.setFill(chosenColor)
    myRectangle.draw(win)
    lastItem = myRectangle


# Drawing/redrawing circles with a given tinkter event
def drawCirc(event):
    global myCircle
    global lastItem
    global chosenColor
    try:
        myCircle.undraw()
    except NameError as e:
        pass

    # Now I have to do math to make sure the circle gets drawn correctly
    aSide = 0
    bSide = 0
    if dragcoordX > event.x:
        aSide = dragcoordX - event.x
    else:
        aSide = event.x - dragcoordX

    if dragcoordY > event.y:
        bSide = dragcoordY - event.y
    else:
        bSide = event.y - dragcoordY

    # a^2 + b^2 = c^2
    # this is assuming that its the correct kind of circle/triangle so we'll see how this goes
    cSide = sqrt((aSide * aSide) + (bSide * bSide))
    myCircle = Circle(Point(dragcoordX, dragcoordY), cSide)
    if chosenColor is None:
        chosenColor = 'black'
    myCircle.setFill(chosenColor)
    myCircle.draw(win)
    lastItem = myCircle


# Drawing/redrawing labels with a given tinkter event
def drawLbl(event):
    global mylabel
    global lastItem
    global chosenColor
    try:
        mylabel.undraw()
    except NameError as e:
        pass
    mylabel = Text(Point(event.x, event.y), "Label")
    if chosenColor is None:
        chosenColor = 'black'
    mylabel.setFill(chosenColor)
    mylabel.draw(win)
    lastItem = mylabel


# delete the last item drawn on the canvas
def undoLast():
    global lastItem
    if lastItem is not None:
        try:
            lastItem.undraw()
            win.delItem(lastItem)
            lastItem = None
        except ValueError as valE:
            pass


def grabInfo(win):
    getFormObjects(win)


# main loop to keep the window alive
while True:
    # constantly check for a new mouse click
    newClick = win.checkMouse()
    if newClick is not None:
        currX = newClick.getX()
        currY = newClick.getY()

        # print(str(currX) + ", " + str(currY))

        # check if they are clicking inside of my selection box
        if 50 <= currX <= 250:
            # user hits the exit button
            if 840 <= currY <= 895:
                exit(0)

            if 50 <= currY <= 450:
                # check if rectangle
                if 80 <= currX <= 210:
                    if 90 <= currY <= 150:
                        win.config(cursor="tcross")
                        win.bind('<B1-Motion>', drawRec)

                # check if circle
                if 80 <= currX <= 200:
                    if 200 <= currY <= 320:
                        win.config(cursor="tcross")
                        win.bind('<B1-Motion>', drawCirc)

                # check if label
                if 100 <= currX <= 181:
                    if 367 <= currY <= 393:
                        win.config(cursor="tcross")
                        win.bind('<B1-Motion>', drawLbl)

                # check if arrow
                if 63 <= currX <= 242:
                    if 430 <= currY <= 450:
                        win.config(cursor="arrow")
                        win.unbind('<B1-Motion>')

            # check if undo button
            if 520 <= currY <= 620:
                undoLast()
                win.config(cursor="arrow")
                win.unbind('<B1-Motion>')

            # check if top row of color pallet
            if 655 <= currY <= 695:
                if 55 <= currX <= 95:
                    chosenColor = 'black'

                if 105 <= currX <= 145:
                    chosenColor = 'red'

                if 155 <= currX <= 195:
                    chosenColor = 'blue'

                if 205 <= currX <= 245:
                    chosenColor = 'green'

            # check if bottom row of color pallet
            if 705 <= currY <= 745:
                if 55 <= currX <= 95:
                    chosenColor = 'white'

                if 105 <= currX <= 145:
                    chosenColor = 'yellow'

                if 155 <= currX <= 195:
                    chosenColor = 'orange'

                if 205 <= currX <= 245:
                    chosenColor = 'purple'

            if 765 <= currY <= 830:
                writeFormCode(win)

        else:
            # Have to have these essentially zero-out the global variables that I need to cleanly draw the shapes
            try:
                myRectangle = Rectangle(Point(0, 0), Point(0, 0))
            except NameError:
                pass
            try:
                myCircle = Circle(Point(0, 0), 0)
            except NameError:
                pass
            try:
                mylabel = Text(Point(0, 0), "")
            except NameError:
                pass
            dragcoordX = currX
            dragcoordY = currY


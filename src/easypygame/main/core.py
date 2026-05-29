import pygame as pyg
import variables as var


# innitiolizes the whole program
def init(width=300, height=300, bg="white", background=None):
    # sets the abbr to the main word
    if background is None:
        background = bg

    # display variable settings
    var._height = height
    var._width = width
    var.background = background
    var.bg = background

    # misc variable settings
    var._isRunning = True

    # checks if any modules fail to load in
    numpass, numfail = pyg.init()

    # temperary until futher notice
    if numfail > 0:
        print("pygames has failed to import all nessasary modules")

    # returns the passes and fails
    return (numpass, numfail)


# gives the height to the user; not allowing any changes to the height
def getHeight():
    return var._height


# gives the width to the user; not allowing any changes to the width
def getWidth():
    return var._width

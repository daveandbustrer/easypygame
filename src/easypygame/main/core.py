import pygame as pyg
from . import variables as var


# sets the variables
def _set_pygame_variables():
    var._display = pyg.display
    time = var._time = pyg.time
    var._events = pyg.event
    var._clock = time.Clock
    var._draw = pyg.draw
    pass


# initilizes the whole program
def init(
    width=300,
    height=300,
    bg="white",
    background=None,
    frame=60,
):
    # sets the abbr to the main word
    if background is None:
        background = bg

    # display variable settings
    var._height = height
    var._width = width
    var._size = (width, height)
    var.background = background
    var.bg = background
    var.frames = frame

    # misc variable settings
    var._isRunning = True

    # checks if any modules fail to load in
    numpass, numfail = pyg.init()

    # temperary until futher notice
    if numfail > 0:
        print("pygames has failed to import all nessasary modules")

    # sets the rest of the needed variables
    _set_pygame_variables()

    # returns the passes and fails
    return (numpass, numfail)


# gives the height to the user; not allowing any changes to the height
def getHeight():
    return var._height


# gives the width to the user; not allowing any changes to the width
def getWidth():
    return var._width


def getDelta():
    return var._dt


def draw(screen):
    shapes = var._shapes
    pydraw = var._draw
    for obj in shapes:
        if obj.type == "circle":
            pydraw.circle(
                obj._screen if not obj._screen is None else screen,
                obj.color,
                pyg.Vector2(obj.x, obj.y),
                obj.radius,
            )
        if obj.type == "rect":
            pydraw.rect(
                obj._screen if not obj._screen is None else screen,
                obj.color,
                (obj.x, obj.y, obj.width, obj.height),
            )


def bind(funcType, func):
    if funcType in var._func:
        var._func[funcType] = func


def unbind(funcType):
    if funcType in var._func:
        var._func[funcType] = None

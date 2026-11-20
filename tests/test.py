from Blu_easypygame import *

init(300, 300)
line = Line(150, 100, 150, 100)
dx: int = 1


def swap():
    global dx
    print(window.width, window.height)
    line.x2 += dx
    if line.x2 > 190 or line.x2 < 10:
        dx *= -1


bind("main", swap)
run()

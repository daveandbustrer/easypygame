import Blu_easypygame as esypy

esypy.init(300, 300)
x: int = 10
y: int = 100
line = esypy.line((x, y), (y, x))


def swap():
    global x
    print("swap worked")
    line.draw()
    line.start = (x, y)
    x += 1


def main():
    esypy.bind("main", swap)
    print("swap failed maybe")


esypy.bind("main", main)
esypy.run()

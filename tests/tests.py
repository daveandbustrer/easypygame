import easypygame as esypy

esypy.init()
x = esypy.graphics.static.circle(100, 100, 10)


def main():
    x.x += 1


esypy.bind("main", main)
esypy.run()

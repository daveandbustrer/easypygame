import easypygame as epy

epy.init(width=600, height=600)
x = epy.graphics.static.circle(100, 100, 100)
width = epy.getWidth()


def main():
    x.x += 1
    x.y += 1
    if x.left > width:
        x.right = 0
    if x.top > width:
        x.bottom = 0


epy.bind("main", main)
epy.run()

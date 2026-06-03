import easypygame as epy

epy.init(width=600, height=600)
x = epy.graphics.rect(100, 100, 100, 100)
y = epy.graphics.ellipse(100, 100, 100, 90)
width = epy.getWidth()
height = epy.getWidth()


def main():
    x.angle += 1
    y.angle += 1
    x.x += 1
    y.y += 1
    if y.y > height or x.x > width:
        x.x = 0
        y.y = 0


epy.bind("main", main)
epy.run()

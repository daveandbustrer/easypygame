import easypygame as epy

epy.init(width=600, height=600)
x = epy.graphics.rect(100, 100, 200, 200)
width = epy.getWidth()
height = epy.getWidth()


def main():
    x.angle += 1
    x.x += 1
    x.y += 1
    if x.y > height or x.x > width:
        x.x = 0
        x.y = 0


epy.bind("main", main)
epy.run()

import easypygame as epy

epy.init(width=600, height=600)
x = epy.graphics.static.rect(100, 100, 100, 100)
width = epy.getWidth()
height = epy.getHeight()


def main():
    x.x += 1
    x.y += 1
    print(x.x, x.y)
    if x.left > width:
        x.right = 0
    if x.top > height:
        x.bottom = 0


epy.bind("main", main)
epy.run()

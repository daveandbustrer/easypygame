import easypygame as epy

epy.init(width=600, height=600)
x = epy.graphics.static.rect(100, 100, 100, 100)
y = epy.graphics.static.circle(100, 100, 100)
width = epy.getWidth()
height = epy.getHeight()


def main():
    x.x += 1
    y.y += 1
    if x.left > width:
        x.right = 0
    if y.top > height:
        y.bottom = 0


def click(event):
    print(event)
    pass


epy.bind("main", main)
epy.bind("leftMouseDown", click)
epy.run()

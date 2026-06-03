import easypygame as epy

epy.init(width=600, height=600)
x = epy.graphics.static.rect(100, 100, 100, 100)
y = epy.graphics.static.circle(100, 100, 50)
v = epy.graphics.static.line([])
width = epy.getWidth()
height = epy.getHeight()
line_list = []


def main():
    x.x += 1
    y.y += 1
    if x.left > width:
        x.right = 0
    if y.top > height:
        y.bottom = 0


def click(event):
    print(event)
    line_list.append(event)
    v.points = line_list
    pass


epy.bind("main", main)
epy.bind("leftMouseDown", click)
epy.run()

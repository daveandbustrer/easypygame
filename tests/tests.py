import easypygame as epy

epy.init(width=600, height=600, frame=600)
x = epy.graphics.square(100, 100, 100, 100)
y = epy.graphics.circle(100, 100, 50)
lines = epy.graphics.polygon(
    [],
)
width = epy.getWidth()
height = epy.getWidth()
xy = []


def main(dt):
    print(dt)
    # xy.append(epy.graphics.ellipse(x.x + y.angle, x.y - x.angle, 100, 50))
    lines.angle += 10 * dt
    for obj in xy:
        obj.x += 10 * dt
        obj.y == 10 * dt
    x.angle += -10 * dt
    y.angle += 10 * dt
    x.x += 100 * dt
    y.y += 100 * dt
    if y.y > height or x.x > width:
        x.x = 0
        y.y = 0


def click(event):
    x, y = event
    lines.add_point(x, y)


epy.bind("main", main)
epy.bind("mouseDown", click)
epy.run()

import easypygame as epy

epy.init(width=600, height=600, frame=60)
x = epy.graphics.square(100, 100, 100, 100)
y = epy.graphics.circle(100, 100, 50)
lines = epy.graphics.polygon(
    [],
)
width = epy.getWidth()
height = epy.getWidth()
xy = []
spin = False

def main(dt):
    global spin
    # xy.append(epy.graphics.ellipse(x.x + y.angle, x.y - x.angle, 100, 50))

    for obj in xy:
        obj.x += 10 * dt
        obj.y += 10 * dt
    if spin:
        x.angle += -10 * dt
        y.angle += 10 * dt
        lines.angle += 10 * dt
    x.x += 100 * dt
    y.y += 100 * dt
    y.x += x.angle*dt
    x.x += y.angle*dt
    if y.top > height or x.left > width:
        x.x = 0
        y.y = 0
        y.x = 0
        x.y = 0


def click(event):
    x, y = event
    lines.add_point(x, y)
def spin_click():
    global spin
    spin = True if not spin else False

epy.bind("mainLoop", main)
epy.bind("mouseDown", click)
epy.bind("rightMouseDown",spin_click)
epy.run()

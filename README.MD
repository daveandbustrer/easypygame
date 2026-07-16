Got you — here’s a **more casual, coder‑friendly README rewrite** that keeps everything clear but drops the formal “documentation voice.” This feels like something you'd see on GitHub from a dev who built a neat helper library for Pygame.

I’ll keep it tight, friendly, and aimed at people who already know how to code.

---

# Blu Easy Pygame

Blu Easy Pygame is a tiny wrapper around `pygame` that removes some setup things. i did this so i can get rid of setup for projects I could do since I have a certain style of coding I do and this project mixes fetures

# Install
```bash
pip install pygame
pip install Blu-easypygame
```

---

# Quick Start

```python
import Blu_easypygame as epy

# Make a window
epy.init(width=640, height=480, bg="lightgray")

# Drop some shapes in
box = epy.graphics.rect(100, 100, 120, 80, color="red")
circle = epy.graphics.circle(300, 200, 50, color="blue")
line = epy.graphics.line([(50, 50), (200, 120)], width=4, color="green")
triangle = epy.graphics.polygon(
    [(350, 100), (420, 180), (320, 220)],
    color="purple"
)

def update(dt):
    box.x += 100 * dt
    if box.left > epy.getWidth():
        box.right = 0

def clicked(event):
    print("Mouse clicked!", event)

epy.bind("mainLoop", update)
epy.bind("leftMouseDown", clicked)

epy.run()
```

---

# main Functions

### `epy.init()`
Sets up the window and starts pygame.

```python
epy.init(width=300, height=300, bg="white", frame=60)
```

### `epy.run()`
Starts the main loop.  
Stops when you close the window or call:

```python
epy.stop()
```

### `epy.bind(event, func)`
Attach your own functions to events.

```python
epy.bind("mainLoop", update)
epy.bind("leftMouseDown", clicked)
```

Supported events include:

- `mainLoop`
- `physicsLoop`
- `mouseDown`, `mouseUp`
- `leftMouseDown`, `rightMouseDown`, etc.
- `mouseMotion`
- `mouseWheel`
- `keyDown`, `keyUp`

### Other stuff

```python
epy.unbind("mainLoop")
epy.getWidth()
epy.getHeight()
epy.getFPS()
epy.getGameTime()
epy.setBackground("black")
epy.sleep(1000)
```

---

# Shapes

shapes will auto draw

### Rectangle
```python
epy.graphics.rect(x, y, w, h, angle=0, color="black")
```

### Circle
```python
epy.graphics.circle(x, y, radius, color="black")
```

### Ellipse
```python
epy.graphics.ellipse(x, y, w, h, angle=0, color="black")
```

### Square
```python
epy.graphics.square(x, y, radius, angle=0, color="black")
```

### Line
```python
epy.graphics.line(points, width=1, color="black")
```

### Polygon
```python
epy.graphics.polygon(points, width=0, angle=0, color="black")
```

---

# Shape Properties

You can change shape properties anytime and they will change in realtime
Common ones:

- `x`, `y`
- `left`, `right`, `top`, `bottom`
- `color`
- `angle`

shapes like circles,lines, and rect also have:
rect
- `width`, `height`
circle
- `radius`
lines
- `points`

Example:

```python
box.x += 5
box.color = "blue"
print(circle.radius)
```

---

# data

Mouse events give you stuff like:

- position  
- pressed buttons  
- movement  
- wheel scroll  

Keyboard events include:

- key  
- unicode  
- modifiers  
- scancode  

Example:

```python
def on_click(event):
    print(event)

epy.bind("leftMouseDown", on_click)
```

---

# Example

```python
import Blu_easypygame as epy

epy.init(width=640, height=480, bg="lightgray")

player = epy.graphics.rect(50, 50, 50, 50, color="blue")

enemy = epy.graphics.polygon(
    [(400, 100), (460, 180), (340, 180)],
    color="red"
)

def update(dt):
    player.x += 120 * dt
    if player.left > epy.getWidth():
        player.right = 0

def on_click(event):
    print(event)

epy.bind("mainLoop", update)
epy.bind("leftMouseDown", on_click)

epy.run()
```

---

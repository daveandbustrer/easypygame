# Blu Easy Pygame

A small wrapper for `pygame` that makes basic game setup easier.

`Blu_easy_pygame` provides:

- a simple `init()` function for window setup
- a single `run()` loop for frame updates
- callback binding for mouse events and frame updates
- ready-made shape classes for rectangles, circles, ellipses, lines, squares, and polygons

---

## Installation

Install `pygame` first, then install this package in editable mode while developing:

```bash
python -m pip install pygame
python -m pip install -e .
```

If the package is published on PyPI, install it with:

```bash
python -m pip install Blu_easy_pygame
```

---

## Quick Start

```python
import easypygame as epy

# 1. Initialize the window
epy.init(width=600, height=600, bg="white")

# 2. Create shapes
box = epy.graphics.static.rect(100, 100, 120, 80, color="red")
circle = epy.graphics.static.circle(300, 200, 50, color="blue")
line = epy.graphics.line([(50, 50), (200, 120)], width=4, color="green")
polygon = epy.graphics.polygon([(350, 100), (420, 180), (320, 220)], color="purple")

# 3. Frame update function

def update(dt):
    box.x += 100 * dt
    if box.left > epy.getWidth():
        box.right = 0

# 4. Mouse event callback

def on_left_click(event):
    print("Left click:", event)

# 5. Bind callbacks
epy.bind("main", update)
epy.bind("leftMouseDown", on_left_click)

# 6. Start the game loop
epy.run()
```

---

## Core API

### `epy.init(width=300, height=300, bg="white", background=None, frame=60)`

Sets up `pygame`, creates the window size, and configures the background color.

Returns:

- `(passed, failed)` from `pygame.init()`

Arguments:

- `width` — window width in pixels
- `height` — window height in pixels
- `bg` — default background color
- `background` — alias for `bg`
- `frame` — target frames per second

Example:

```python
epy.init(width=800, height=600, bg="black", frame=60)
```

### `epy.run()`

Starts the main game loop.

The loop continues until the player closes the window or `epy.stop()` is called.

Example:

```python
epy.run()
```

### `epy.bind(funcType, func)`

Registers a callback for a supported event type.

Supported `funcType` values:

- `main` — called every frame, receives `dt` milliseconds as a parameter
- `mouseDown` — called when any mouse button is pressed
- `leftMouseDown` — called when the left mouse button is pressed
- `middleMouseDown` — called when the middle mouse button is pressed
- `rightMouseDown` — called when the right mouse button is pressed

Example:

```python
def update(dt):
    print("Delta time:", dt)

epy.bind("main", update)
```

Example mouse callback:

```python
def on_click(event):
    print("Mouse event:", event)

epy.bind("leftMouseDown", on_click)
```

### `epy.unbind(funcType)`

Removes the callback for the given event type.

Example:

```python
epy.unbind("leftMouseDown")
```

### `epy.stop()`

Stops the game loop from inside a callback.

Example:

```python
def quit_game(dt):
    epy.stop()

epy.bind("main", quit_game)
```

### `epy.getWidth()` and `epy.getHeight()`

Return the window width and height set by `init()`.

Example:

```python
width = epy.getWidth()
height = epy.getHeight()
```

### `epy.getDelta()`

Returns the time in seconds since the last frame.

Example:

```python
dt = epy.getDelta()
```

### `epy.background`

Global background color. You can modify it during the game.

Example:

```python
epy.background = "black"
```

### `epy.frames`

Global frame rate limit. Set it before calling `epy.run()`.

Example:

```python
epy.frames = 30
```

---

## Shapes

There are two ways to create shapes:

- `epy.graphics.static` for basic static shapes
- `epy.graphics` for direct shape classes, including advanced shapes like `line` and `polygon`

### `epy.graphics.static.rect(x, y, width, height, color="black")`

Create a rectangle.

Example:

```python
rect = epy.graphics.static.rect(50, 50, 120, 80, color="red")
```

### `epy.graphics.static.circle(x, y, radius, color="black")`

Create a circle.

Example:

```python
circle = epy.graphics.static.circle(200, 200, 50, color="blue")
```

### `epy.graphics.ellipse(x, y, width, height, angle=0, color="black")`

Create an ellipse.

Example:

```python
egg = epy.graphics.ellipse(300, 150, 160, 80, angle=0, color="green")
```

### `epy.graphics.rect(x, y, width, height, angle=0, color="black")`

Create a rotated rectangle.

Example:

```python
box = epy.graphics.rect(250, 250, 120, 80, angle=45, color="orange")
```

### `epy.graphics.square(x, y, radius, angle=0, color="black")`

Create a square.

Example:

```python
square = epy.graphics.square(150, 300, 50, angle=30, color="purple")
```

### `epy.graphics.line(points, width=1, color="black")`

Create a polyline from points.

Example:

```python
line = epy.graphics.line([(50, 400), (200, 450), (300, 380)], width=3, color="yellow")
```

### `epy.graphics.polygon(points, width=0, angle=0, color="black")`

Create a polygon with a list of points.

Example:

```python
triangle = epy.graphics.polygon(
    [(350, 100), (420, 180), (320, 220)],
    color="purple"
)
```

Add more points later:

```python
triangle.add_point(380, 50)
```

---

## Shape Properties

Most shapes expose these properties:

- `x`, `y`
- `left`, `right`, `top`, `bottom`
- `width`, `height` for rectangles and ellipses
- `radius` for circles
- `points` for lines and polygons
- `angle` for rotated shapes
- `color`

Example:

```python
rect.x += 5
rect.color = "blue"
print(circle.radius)
```

---

## Mouse event data

Mouse callbacks receive either a position tuple or a dictionary.

When a simple click event is available, the callback may receive:

```python
(100, 200)
```

If touch or window metadata is present, the callback receives a dictionary:

```python
{"pos": (100, 200), "touch": ..., "window": ...}
```

Example:

```python
def on_click(event):
    print("Clicked:", event)
```

---

## Tips

- Use `epy.bind("main", update)` to run code every frame.
- Use `epy.bind("leftMouseDown", callback)` for left-click interactions.
- Use `epy.stop()` to exit the loop from inside a callback.
- Use `epy.getWidth()` and `epy.getHeight()` to keep objects inside the window.

---

## Full example

```python
import easypygame as epy

# Initialize
epy.init(width=640, height=480, bg="lightgray")

# Create shapes
player = epy.graphics.static.rect(50, 50, 50, 50, color="blue")
enemy = epy.graphics.polygon(
    [(400, 100), (460, 180), (340, 180)],
    color="red"
)

# Frame update

def update(dt):
    player.x += 120 * dt
    if player.left > epy.getWidth():
        player.right = 0

# Click event

def on_click(event):
    print("Click event:", event)

# Bind and run
epy.bind("main", update)
epy.bind("leftMouseDown", on_click)
epy.run()
```

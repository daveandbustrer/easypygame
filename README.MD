# Blu Easy Pygame

A lightweight wrapper around `pygame` for a simpler game loop, drawing system, and mouse event binding.

## Overview

`Blu_easy_pygame` makes it easier to build small Python games using a minimal API:

- `init()` sets up the window and frame rate
- `run()` starts the game loop
- `bind()` attaches update and mouse event callbacks
- `graphics.static` provides simple shape objects for circles and rectangles
- `graphics` provides additional shape types such as `polygon`

## Installation

This project relies on `pygame`. Install `pygame` first, then install the package locally.

```bash
python -m pip install pygame
python -m pip install -e .
```

If the package is published to PyPI, you can also install it with:

```bash
python -m pip install Blu_easy_pygame
```

## Quick Start

```python
import easypygame as epy

# Initialize the window
epy.init(width=600, height=600, bg="white")

# Create shapes
x = epy.graphics.static.rect(100, 100, 100, 100)
y = epy.graphics.static.circle(100, 100, 100)
triangle = epy.graphics.polygon([(150, 150), (250, 150), (200, 50)], color="blue")

# Access window size
width = epy.getWidth()
height = epy.getHeight()

# Update function called every frame

def main():
    x.x += 1
    y.y += 1
    if x.left > width:
        x.right = 0
    if y.top > height:
        y.bottom = 0

# Mouse event handler

def click(event):
    print(event)

# Bind callbacks
epy.bind("main", main)
epy.bind("leftMouseDown", click)

# Start the game loop
epy.run()
```

## API Reference

### `init(width=300, height=300, bg="white", background=None, frame=60)`

Initializes the game environment and returns a tuple `(passed, failed)` from `pygame.init()`.

- `width`: window width in pixels
- `height`: window height in pixels
- `bg`: default background color
- `background`: alias for `bg`
- `frame`: target frame rate

### `run()`

Starts the main loop and keeps the window open until the user closes it or `stop()` is called.

### `bind(funcType, func)`

Attaches a callback for a supported function type.

Supported `funcType` values:

- `main` — called each frame
- `mouseDown` — called on any mouse button press
- `leftMouseDown` — called on left mouse button press
- `middleMouseDown` — called on middle mouse button press
- `rightMouseDown` — called on right mouse button press

### `unbind(funcType)`

Removes a previously bound callback for the given function type.

### `stop()`

Stops the game loop and exits cleanly.

### `getWidth()` and `getHeight()`

Return the initialized window dimensions.

### `getDelta()`

Returns the elapsed time in seconds since the last frame.

### `background`

A global variable for the current background color. You can change it at runtime:

```python
epy.background = "black"
```

### `frames`

A global frame-rate target. Change it before calling `run()` if you want a different update speed.

## Graphics Shapes

### `epy.graphics.static.rect(x, y, width, height, color="black")`

Creates a rectangle shape.

- `x`, `y`: position
- `width`, `height`: shape size
- `color`: fill color

### `epy.graphics.static.circle(x, y, radius, color="black")`

Creates a circle shape.

- `x`, `y`: center position
- `radius`: circle radius
- `color`: fill color

### `epy.graphics.polygon(points, width=0, angle=0, color="black")`

Creates a polygon shape from a list of points.

- `points`: a list of `(x, y)` tuples
- `width`: line width; use `0` for a filled polygon
- `angle`: rotation angle in degrees
- `color`: fill or outline color

Use `add_point(x, y)` to append additional vertices after creation.

### Shape Properties

Shapes expose these properties:

- `x`, `y`
- `left`, `right`, `top`, `bottom`
- `color`
- `width`, `height` for rectangles
- `radius` for circles
- `points` for `line` and `polygon` shapes
- `angle` for rotated `polygon` shapes

## Event Parameter

Mouse callbacks receive a dictionary with:

- `pos`: mouse position
- `touch`: touch information when available
- `window`: window event information when available

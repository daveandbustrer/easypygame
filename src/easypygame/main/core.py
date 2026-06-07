from __future__ import annotations

from typing import Any, Callable, Tuple
import pygame as pyg
from . import variables as var


def _set_pygame_variables() -> None:
    """Set the pygame modules and helpers used by the engine."""
    var._display = pyg.display
    time = var._time = pyg.time
    var._events = pyg.event
    var._clock = time.Clock
    var._draw = pyg.draw
    var._transform = pyg.transform


def init(
    width: int = 300,
    height: int = 300,
    bg: str = "white",
    background: str | None = None,
    frame: int = 60,
    busy: bool = False
) -> Tuple[int, int]:
    """Initialize pygame and configure the display and timing values."""
    if background is None:
        background = bg

    var._height = height
    var._width = width
    var._size = (width, height)
    var.background = background
    var.bg = background
    var.frames = frame
    var._isRunning = True
    var._busy = busy

    numpass, numfail = pyg.init()
    if numfail > 0:
        print("pygame failed to initialize some modules")

    _set_pygame_variables()
    return numpass, numfail


def getHeight() -> int | None:
    """Return the current window height after initialization."""
    return var._height


def getWidth() -> int | None:
    """Return the current window width after initialization."""
    return var._width

def getFPS():
    return var._fps

def getGameTime():
    return var._time.get_ticks()

def sleep(miliseconds:int,processOS:bool = True):
    if processOS:
        var._time.wait(miliseconds)
    else:
        var._time.delay(miliseconds)





def draw(screen: pyg.Surface) -> None:
    """Draw all registered shapes to the given surface."""
    shapes = var._shapes
    pydraw = var._draw
    for obj in shapes:
        if obj._type == "shape":
            rotated = var._transform.rotate(obj._surf, obj.angle)
            rect = rotated.get_rect(center=(obj.x, obj.y))
            screen.blit(rotated, rect)
        elif obj._type == "line":
            if len(obj.points) < 2:
                continue
            pyg.draw.lines(screen, obj.color, obj._line_closed, obj.points, obj.width)
        elif obj._type == "poly":
            if len(obj.points) < 3:
                continue
            obj._polygon__set_surf()
            rotated = var._transform.rotate(obj._surf, obj.angle)
            rect = rotated.get_rect(center=(var._width / 2, var._height / 2))
            screen.blit(rotated, rect)


def bind(funcType: str, func: Callable[..., Any]) -> None:
    """Register a callback for a supported event type."""
    if funcType in var._func:
        var._func[funcType] = func


def unbind(funcType: str) -> None:
    """Remove a callback for a supported event type."""
    if funcType in var._func:
        var._func[funcType] = None


def stop() -> None:
    """Stop the running game loop."""
    var._isRunning = False

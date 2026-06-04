from __future__ import annotations

import pygame as pyg
from . import core, events, variables as var


def run() -> None:
    """Start the main game loop and render frames until the window closes."""
    if not var._isRunning:
        return

    display = var._display
    clock = var._clock()
    screen = var._screen = display.set_mode(var._size)

    while var._isRunning:
        screen.fill(var.background)
        core.draw(screen)
        events.all_events()
        core.draw(screen)
        display.flip()
        var._dt = clock.tick(var.frames) / 1000

    pyg.quit()

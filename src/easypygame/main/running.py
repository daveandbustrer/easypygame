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

        events.all_events()
        
        screen.fill(var.background)
        core.draw(screen)
        display.flip()

        if var._busy:
            clock.tick_busy_loop()
        else:
            clock.tick(var.frames)

        var._game_dt = clock.get_time()
        var._physic_dt = clock.get_rawtime()

        var._fps = clock.get_fps()


    pyg.quit()

from . import variables as var
import pygame as pyg


def run():

    isRunning = var._isRunning

    if isRunning is not None:

        display = var._display
        clock = var._clock()
        events = var._events

        screen = var._screen = display.set_mode(var._size)

        while isRunning:
            for event in events.get():
                if event.type == pyg.QUIT:
                    isRunning = False

            screen.fill(var.background)

            # RENDER YOUR GAME HERE

            display.flip()

            var._dt = clock.tick(var.frames) / 1000

        pyg.quit()
    pass

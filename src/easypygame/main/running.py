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

            # fill the screen with a color to wipe away anything from last frame
            screen.fill(var.background)

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            display.flip()

            clock.tick(var.frames)  # limits FPS to 60

        pyg.quit()
    pass

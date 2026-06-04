from . import variables as var,core,events
import pygame as pyg


def run():

    if var._isRunning is not None:

        display = var._display
        clock = var._clock()

        screen = var._screen = display.set_mode(var._size)
        while var._isRunning:

            screen.fill(var.background)

            core.draw(screen)

            events.all_events()

            core.draw(screen)

            # puts evrything on the screen
            display.flip()

            # gets the delta time
            var._dt = clock.tick(var.frames) / 1000

        pyg.quit()
    pass

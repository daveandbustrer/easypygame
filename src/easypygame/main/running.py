from . import variables as var
from . import core
import pygame as pyg
import inspect as ins


def get_click_event(event):
    parameter = {}
    if event.touch:
        parameter["touch"] = event.touch
    if event.window:
        parameter["window"] = event.window
    if parameter:
        parameter["pos"] = event.pos
        return parameter
    else:
        return event.pos


def run_func(func, parameter):
    sig = ins.signature(func)
    if sig.parameters:
        func(parameter)
    else:
        func()


def run():

    if var._isRunning is not None:

        display = var._display
        clock = var._clock()
        events = var._events

        screen = var._screen = display.set_mode(var._size)
        funcs = var._func
        while var._isRunning:

            for event in events.get():
                if event.type == pyg.QUIT:
                    var._isRunning = False
                if event.type == pyg.MOUSEBUTTONDOWN:
                    parameter = get_click_event(event)
                    if event.button != 4 or event.button != 5:
                        if funcs["mouseDown"]:
                            run_func(funcs["mouseDown"], parameter)
                        if event.button == 1:
                            if funcs["leftMouseDown"]:
                                run_func(funcs["leftMouseDown"], parameter)
                        if event.button == 2:
                            if funcs["middleMouseDown"]:
                                run_func(funcs["middleMouseDown"], parameter)
                        if event.button == 3:
                            if funcs["rightMouseDown"]:
                                run_func(funcs["rightMouseDown"], parameter)
                    else:
                        pass

            screen.fill(var.background)

            core.draw(screen)

            if funcs["main"]:
                run_func(funcs["main"], var._dt)

            core.draw(screen)

            # puts evrything on the screen
            display.flip()

            # gets the delta time
            var._dt = clock.tick(var.frames) / 1000

        pyg.quit()
    pass

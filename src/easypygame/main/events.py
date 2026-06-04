from .callback import run_event,get_click_event
from . import variables as var
import pygame as pyg


def pygame_events():
    events = var._events
    for event in events.get():
        if event.type == pyg.QUIT:
            var._isRunning = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            parameter = get_click_event(event)

            if event.button == 4 or event.button == 5:
                continue

            run_event("mouseDown",parameter)
            if event.button == 1:
                run_event("leftMouseDown",parameter)
            elif event.button == 2:
                run_event("middleMouseDown",parameter)
            elif event.button == 3:
                run_event("rightMouseDown",parameter)

def loop_event():
    run_event("main",var._dt)

def all_events():
    pygame_events()
    loop_event()
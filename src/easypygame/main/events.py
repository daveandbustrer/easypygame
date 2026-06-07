from __future__ import annotations

from typing import Any
import pygame as pyg
from .callback import get_click_parameter, get_wheel_parameter, get_key_parameter, run_event
from . import variables as var

def run_click_events(upOrDown:str, event:any):
    if event.button in (4, 5):
            return

    parameter = get_click_parameter(event)
    run_event("mouse"+upOrDown, parameter)
    if event.button == 1:
        run_event("leftMouse"+upOrDown, parameter)
    elif event.button == 2:
        run_event("middleMouse"+upOrDown, parameter)
    elif event.button == 3:
        run_event("rightMouse"+upOrDown, parameter)

def run_key_event(upOrDown:str, event:any):
    parameter = get_key_parameter()
    run_event("key"+upOrDown,parameter)


def pygame_events() -> None:
    """Read pygame events and dispatch matching callbacks."""
    events = var._events
    if events is None:
        return

    for event in events.get():
        #quit
        if event.type == pyg.QUIT:
            var._isRunning = False
        #mouse down
        elif event.type == pyg.MOUSEBUTTONDOWN:
            run_click_events("Down",event)
        #mouse up
        elif event.type == pyg.MOUSEBUTTONUP:
            run_click_events("Up",event)
        elif event.type == pyg.MOUSEMOTION:
            parameter = get_click_parameter(event)
            run_event("mouseMotion",parameter)
        #mouse wheel
        elif event.type == pyg.MOUSEWHEEL:
            parameter = get_wheel_parameter(event)
            run_event("mouseWheel",parameter)
        elif event.type == pyg.KEYDOWN:
            run_key_event("Down",event)
        elif event.type == pyg.KEYUP:
            run_key_event("Up",event)



def loop_event() -> None:
    """Trigger a frame update callback each loop iteration."""
    run_event("mainLoop", var._game_dt/1000)
    run_event("phisicLoop",var._physic_dt/1000)


def all_events() -> None:
    """Process input and then run the frame callback."""
    pygame_events()
    loop_event()
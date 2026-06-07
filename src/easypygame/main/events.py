from __future__ import annotations

from typing import Any
import pygame as pyg
from .callback import get_click_event, run_event
from . import variables as var


def pygame_events() -> None:
    """Read pygame events and dispatch matching callbacks."""
    events = var._events
    if events is None:
        return

    for event in events.get():
        if event.type == pyg.QUIT:
            var._isRunning = False
        elif event.type == pyg.MOUSEBUTTONDOWN:
            if event.button in (4, 5):
                continue

            parameter = get_click_parameter(event)
            run_event("mouseDown", parameter)
            if event.button == 1:
                run_event("leftMouseDown", parameter)
            elif event.button == 2:
                run_event("middleMouseDown", parameter)
            elif event.button == 3:
                run_event("rightMouseDown", parameter)
        elif event.type == pyg.MOUSEWHEEL:
            parameter = get_wheel_parameter(event)
            run_event("mouseWheel",parameter)


def loop_event() -> None:
    """Trigger a frame update callback each loop iteration."""
    run_event("mainLoop", var._game_dt/1000)
    run_event("phisicLoop",var._physic_dt/1000)


def all_events() -> None:
    """Process input and then run the frame callback."""
    pygame_events()
    loop_event()
from __future__ import annotations

import inspect as ins
from typing import Any, Callable, Dict, Tuple, Union
from . import variables as var


def run_event(event: str, parameter: Any) -> None:
    """Call a bound callback for the given event type."""
    funcs = var._func
    callback = funcs.get(event)
    if callback is not None:
        run_func(callback, parameter)


def get_click_parameter(event: Any) -> Union[Dict[str, Any], Tuple[int, int]]:
    """Extract click data from a pygame event object."""
    parameter: Dict[str, Any] = {}
    if event.touch:
        parameter["touch"] = event.touch
    if event.window:
        parameter["window"] = event.window

    if parameter:
        parameter["pos"] = event.pos
        return parameter

    return event.pos

def get_wheel_parameter(event:any):
    parameter: Dict[str, Any] = {}
    if event.touch:
        parameter["touch"] = event.touch
    if event.window:
        parameter["window"] = event.window
    if event.flipped:
        parameter["flipped"] = event.flipped
    if event.x:
        parameter["x"] = event.x if not event.precise_x in [1,-1] else event.precise_x
    
    y = event.y if not event.precise_y in [1,-1] else event.precise_y
    if parameter:
        parameter["y"] = y
        return parameter

    return y
    

def run_func(func: Callable[..., Any], parameter: Any) -> None:
    """Execute a callback with or without an argument."""
    sig = ins.signature(func)
    if sig.parameters:
        func(parameter)
    else:
        func()
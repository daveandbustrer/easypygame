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

def get_extra_parameter(event,parameter):
    if hasattr(event,"touch"):
        if event.touch:
            parameter["touch"] = event.touch
    if event.window:
        parameter["window"] = event.window
    return parameter
        
def get_click_parameter(event: Any) -> Union[Dict[str, Any], Tuple[int, int]]:
    """Extract click data from a pygame event object."""
    parameter: Dict[str, Any] = {}
    get_extra_parameter(event, parameter)
    if hasattr(event,"rel"):
        parameter["rel"] = event.rel
    if hasattr(event,"buttons"):
        parameter["buttons"] = event.buttons
    
    parameter["pos"] = event.pos
    return parameter

def get_wheel_parameter(event:any):
    parameter: Dict[str, Any] = {}
    get_extra_parameter(event, parameter)
    if event.flipped:
        parameter["flipped"] = event.flipped
    if event.x:
        parameter["x"] = event.x if not event.precise_x in (1,-1) else event.precise_x
    
    parameter["y"] = event.y if not event.precise_y in (1,-1) else event.precise_y
    return parameter

def get_key_parameter(event:any):
    parameter: Dict[str,Any] = {}
    get_extra_parameter(event, parameter)
    parameter["unicode"] = event.unicode
    parameter["key"] = event.key
    parameter["mod"] = event.mod
    parameter["scancode"] = event.scancode
    return parameter
    

def run_func(func: Callable[..., Any], parameter: Any) -> None:
    """Execute a callback with or without an argument."""
    sig = ins.signature(func)
    if sig.parameters:
        func(parameter)
    else:
        func()
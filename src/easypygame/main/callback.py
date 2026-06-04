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


def get_click_event(event: Any) -> Union[Dict[str, Any], Tuple[int, int]]:
    """Extract click data from a pygame event object."""
    parameter: Dict[str, Any] = {}
    if hasattr(event, "touch") and event.touch:
        parameter["touch"] = event.touch
    if hasattr(event, "window") and event.window:
        parameter["window"] = event.window

    if parameter:
        parameter["pos"] = event.pos
        return parameter

    return event.pos


def run_func(func: Callable[..., Any], parameter: Any) -> None:
    """Execute a callback with or without an argument."""
    sig = ins.signature(func)
    if sig.parameters:
        func(parameter)
    else:
        func()
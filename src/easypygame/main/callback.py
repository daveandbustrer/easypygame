import inspect as ins
from . import variables as var

def run_event(event,parameter):
    funcs = var._func
    if funcs[event]:
            run_func(funcs[event], parameter)

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
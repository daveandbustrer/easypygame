from ._version import version as __version__
from . import graphics
from .main.core import init, getHeight, getWidth, bind, unbind, stop,getFPS,sleep,getGameTime
from .main.variables import background,maxFrames
from .main.running import run

__all__ = [
    "graphics",
    "run",
    "background",
    "init",
    "getHeight",
    "getWidth",
    "bind",
    "unbind",
    "stop",
    "maxFrames",
    "getFPS",
    "sleep",
    "getGameTime"
]

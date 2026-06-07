from ._version import version as __version__
from . import graphics
from .main.core import init, getHeight, getWidth, bind, unbind, stop, getFPS, sleep, getGameTime,getBackground,setBackground
from .main.variables import maxFrames
from .main.running import run

__all__ = [
    "graphics",
    "run",
    "init",
    "getHeight",
    "getWidth",
    "bind",
    "unbind",
    "stop",
    "maxFrames",
    "getFPS",
    "sleep",
    "getGameTime",
    "setBackground",
    "getBackground"
]

from ._version import version as __version__
from . import graphics
from .main.core import init, getHeight, getWidth
from .main.variables import bg, background
from .main.running import running

__all__ = ["graphics", "running", "bg", "background", "init", "getHeight", "getWidth"]

from ._version import version as __version__
from . import graphics
from .main.core import init, getHeight, getWidth
from .main.variables import background
from .main.running import run

__all__ = ["graphics", "run", "background", "init", "getHeight", "getWidth"]

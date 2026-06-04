from __future__ import annotations

from typing import Any
import pygame as pyg
from easypygame.main import variables as vars
from .shape import shape


class ellipse(shape):
    """A drawable ellipse shape."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        angle: int = 0,
        color: str = "black",
    ) -> None:
        super().__init__(x, y, width, height, angle, color)
        self._surf: pyg.Surface = pyg.Surface((self.width, self.height), pyg.SRCALPHA)
        vars._draw.ellipse(self._surf, self.color, (0, 0, self.width, self.height))
        vars._shapes.append(self)

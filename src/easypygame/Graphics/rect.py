from __future__ import annotations

import pygame as pyg
from easypygame.main import variables as vars
from .shape import shape


def get_avg(v1: int, v2: int) -> float:
    return (v1 + v2) / 2


def get_sub(v1: int, v2: int) -> int:
    return int(v2 - v1)


class rect(shape):
    """A drawable rectangle shape."""

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
        vars._draw.rect(self._surf, self.color, (0, 0, self.width, self.height))
        vars._shapes.append(self)

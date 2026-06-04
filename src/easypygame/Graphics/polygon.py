from __future__ import annotations

from typing import List, Tuple
import pygame as pyg
from easypygame.main import variables as vars
from .line import line


class polygon(line):
    """A drawable polygon shape built from a list of points."""

    def __init__(
        self,
        points: List[Tuple[int, int]],
        width: int = 0,
        angle: int = 0,
        color: str = "black",
    ) -> None:
        super().__init__(points, width, color)
        self._line_closed = True
        self._type = "poly"
        self._surf: pyg.Surface | None = None
        self.angle = angle
        self.width = width
        self.__set_surf()
        vars._shapes.append(self)

    def add_point(self, x: int, y: int) -> None:
        """Add a new vertex to the polygon."""
        super().add_point(x, y)
        self.__set_surf()

    def __set_surf(self) -> None:
        """Create or update the polygon surface from its points."""
        if len(self.points) > 2 and vars._width and vars._height:
            self._surf = pyg.Surface((vars._width, vars._height), pyg.SRCALPHA)
            vars._draw.polygon(self._surf, self.color, self.points, self.width)

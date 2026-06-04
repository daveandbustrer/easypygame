from __future__ import annotations

from typing import List, Tuple
from easypygame.main import variables as vars


class line:
    """A drawable polyline made of connected points."""

    def __init__(
        self,
        points: List[Tuple[int, int]],
        width: int = 1,
        color: str = "black",
    ) -> None:
        self.points: List[Tuple[int, int]] = points
        self.color = color
        self._type = "line"
        self._line_closed = False
        self.width = width
        vars._shapes.append(self)

    def add_point(self, x: int, y: int) -> None:
        self.points.append((x, y))

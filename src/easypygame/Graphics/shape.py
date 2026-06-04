from __future__ import annotations

from typing import Any


class shape:
    """Base class for drawable shapes."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        angle: int = 0,
        color: str = "black",
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.color = color
        self._type = "shape"
        self._surf: Any = None

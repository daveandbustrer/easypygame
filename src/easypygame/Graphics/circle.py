from __future__ import annotations

from .ellipse import ellipse


class circle(ellipse):
    """A drawable circle shape."""

    def __init__(self, x: int, y: int, radius: int, color: str = "black") -> None:
        super().__init__(x, y, radius * 2, radius * 2, 0, color)

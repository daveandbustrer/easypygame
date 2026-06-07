from __future__ import annotations

from .rect import rect


class square(rect):
    """A drawable square shape."""

    def __init__(
        self,
        x: int,
        y: int,
        radius: int,
        angle: int = 0,
        color: str = "black",
    ) -> None:
        super().__init__(x, y, radius, radius, angle, color)
        self.radius = radius

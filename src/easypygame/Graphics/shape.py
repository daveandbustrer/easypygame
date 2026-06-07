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

    
    @property
    def top(self):
        return self.y - self.height/2
    
    @top.setter
    def top(self,value):
        self.y = value + self.height/2
    
    @property
    def bottom(self):
        return self.y + self.height/2
    
    @bottom.setter
    def bottom(self,value):
        self.y = value - self.height/2
    
    @property
    def left(self):
        return self.x -self.width/2
    
    @left.setter
    def left(self,value):
        self.x = value + self.width/2
    
    @property
    def right(self):
        return self.x + self.width/2
    
    @right.setter
    def right(self,value):
        self.x = value - self.width/2

from .base import shape
from easypygame.main import variables as var


class rect(shape):
    def __init__(self, x, y, width, height, color="black"):
        super().__init__(x, y, width, height, color, None)
        self.width = width
        self.height = height
        self.type = "rect"
        var._shapes.append(self)

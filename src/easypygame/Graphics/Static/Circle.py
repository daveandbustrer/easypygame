from .base import shape
from easypygame.main import variables as var


class circle(shape):
    def __init__(self, x, y, radius, color="black"):
        super().__init__(x, y, radius, radius, color, None)
        self.type = "circle"
        self.radius = radius

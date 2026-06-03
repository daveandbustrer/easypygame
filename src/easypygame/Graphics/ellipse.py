from easypygame.main import variables as vars
from .shape import shape
import pygame as pyg


class ellipse(shape):
    def __init__(self, x, y, width, height, angle=0, color="black"):
        super().__init__(x, y, width, height, angle, color)

        self._surf = pyg.Surface((self.width, self.height), pyg.SRCALPHA)
        vars._draw.ellipse(self._surf, self.color, (0, 0, self.width, self.height))

        vars._shapes.append(self)

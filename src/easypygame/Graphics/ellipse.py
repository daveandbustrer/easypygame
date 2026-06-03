from easypygame.main import variables as vars
import pygame as pyg


class ellipse:
    def __init__(self, x, y, width, height, angle=0, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.color = color

        self._surf = pyg.Surface((self.width, self.height), pyg.SRCALPHA)
        vars._draw.ellipse(self._surf, self.color, (0, 0, self.width, self.height))

        vars._shapes.append(self)

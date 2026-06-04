from easypygame.main import variables as vars
from .line import line
import pygame as pyg


class polygon(line):

    def __init__(self, points, width=0, angle=0, color="black"):
        super().__init__(points, width, color)
        self._line_closed = True
        self._type = "poly"
        self._surf = None
        self.angle = angle
        self.width = width

        self.__set_surf()

        vars._shapes.append(self)

    def add_point(self, x, y):
        super().add_point(x, y)
        self.__set_surf()

    def __set_surf(self):
        if len(self.points) > 2:
            self._surf = pyg.Surface((vars._width, vars._height), pyg.SRCALPHA)
            vars._draw.polygon(self._surf, self.color, self.points, self.width)

from easypygame.main import variables as vars
import pygame as pyg


def get_avg(v1, v2):
    return (v1 + v2) / 2


def get_sub(v1, v2):
    return int(v2 - v1)


class rect:

    def __init__(self, x1, y1, x2, y2, angle=0, color="black"):
        self.x = get_avg(x1, x2)
        self.y = get_avg(y1, y2)
        self.width = get_sub(x1, x2)
        self.height = get_sub(y1, y2)
        self.angle = angle
        self.color = color
        self._surf = pyg.Surface((self.width, self.height), pyg.SRCALPHA)
        vars._draw.rect(self._surf, self.color, (0, 0, self.width, self.height))

        vars._shapes.append(self)
        pass

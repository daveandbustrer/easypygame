from . import var
import pygame


class Line:
    def __init__(
        self,
        x1: var.num,
        y1: var.num,
        x2: var.num,
        y2: var.num,
        color: var.color = "black",
    ) -> None:
        self.x1 = x1
        self.y1 = x1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.index = len(var.draw)
        var.draw.append(self)

    def _draw(self):
        if var.screen:
            pygame.draw.line(
                var.screen, self.color, (self.x1, self.y1), (self.x2, self.y2)
            )

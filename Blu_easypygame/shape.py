from . import var
import pygame


class line:
    def __init__(
        self,
        start: list[var.num] | tuple[var.num, var.num],
        end: list[var.num] | tuple[var.num, var.num],
        color: var.color = "black",
    ) -> None:
        self.start = start
        self.end = end
        self.color = color

    def draw(self):
        if var.screen:
            pygame.draw.line(var.screen, self.color, self.start, self.end)

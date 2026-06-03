from .ellipse import ellipse


class circle(ellipse):
    def __init__(self, x, y, radius, color="black"):
        super().__init__(x, y, radius * 2, radius * 2, 0, color)

from .rect import rect


class square(rect):
    def __init__(self, x, y, radius, angle=0, color="black"):
        super().__init__(x, y, radius, radius, angle, color)
        pass

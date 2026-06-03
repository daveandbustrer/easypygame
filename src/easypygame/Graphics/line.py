from easypygame.main import variables as vars


class line:
    def __init__(self, points, color="black"):
        self.points = [(i, i + 1) for i in range(0, len(points) - 1)]
        self.color = color
        self._type = "line"
        self._line_closed = False

        vars._shapes.append(self)

    def add_point(self, x, y):
        self.points.append((x, y))

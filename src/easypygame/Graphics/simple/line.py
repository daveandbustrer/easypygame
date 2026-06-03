from easypygame.main import variables as var


class line:
    def __init__(self, points, width=1, color="black"):
        self.points = [
            (points[i], points[i + 1])
            for i in range(len(points))
            if i + 1 < len(points)
        ]
        self.width = width
        self.color = color
        self._screen = None
        self.type = "line"
        var._shapes.append(self)
        pass

class line:
    def line(points, color="black"):
        self.points = [(i, i + 1) for i in range(0, len(points) - 1)]
        self.color = color
        self._type = "line"

        vars._shapes.append(self)

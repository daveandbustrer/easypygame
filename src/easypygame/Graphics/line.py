from easypygame.main import variables as vars
import math


class line:
    def __init__(self, points, angle=0, color="black"):
        self.points = [(i, i + 1) for i in range(0, len(points) - 1)]
        self.color = color
        self._angle = angle
        self._type = "line"
        self.__closed = False

        vars._shapes.append(self)

    def rotate_points(self):
        # pivot = center of all points
        if len(self.points) < 1:
            return

        cx = sum(p[0] for p in self.points) / len(self.points)
        cy = sum(p[1] for p in self.points) / len(self.points)

        rad = math.radians(self.angle / vars.frames)

        rotated_points = []
        for px, py in self.points:
            dx = px - cx
            dy = py - cy
            rx = cx + dx * math.cos(rad) - dy * math.sin(rad)
            ry = cy + dx * math.sin(rad) + dy * math.cos(rad)
            rotated_points.append((rx, ry))
        self.points = rotated_points

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value % 360
        print(value)
        self.rotate_points()

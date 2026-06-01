class shape:
    def __init__(self, x, y, width, height, color):
        self._x = x
        self._y = y
        self.width = width
        self.height = height
        self._left = x - width
        self._right = x + width
        self._top = y - height
        self._bottom = y + height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._left = value - self.width
        self._right = value + self.width

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._x = value + self.width
        self._right = value + self.width + self.width
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._x = value - self.width
        self._right = value
        self._left = value - self.width - self.width

    @property
    def y(self):
        return self._y

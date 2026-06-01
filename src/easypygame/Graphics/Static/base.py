class shape:
    def __init__(self, x, y, width, height, color, screen):
        self._screen = screen
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._left = x - width
        self._right = x + width
        self._top = y - height
        self._bottom = y + height
        self.color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._left = value - self._width
        self._right = value + self._width

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._x = value + self._width
        self._right = value + self._width + self._width
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._x = value - self._width
        self._right = value
        self._left = value - self._width - self._width

    @property
    def y(self):
        return self._y

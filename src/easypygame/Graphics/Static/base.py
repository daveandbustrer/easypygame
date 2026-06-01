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

    @y.setter
    def y(self, value):
        self._y = value
        self._top = value - self._height
        self._bottom = value + self._height

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top = value
        self._y = value + self._height
        self._bottom = value + self._height + self._height

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        self._bottom = value
        self._y = value - self._height
        self._top = value - self._height - self._height

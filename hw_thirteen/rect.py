from exceptions import RectangleTypeError, RectangleValueError

class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            width = length
        self.check_side(length)
        self.check_side(width)
        self.length = length
        self.width = width

    @staticmethod
    def check_side(value):
        if not isinstance(value, int):
            raise RectangleTypeError(value)
        if value <= 0:
            raise RectangleValueError(value)

    def perimeter(self):
        return 2 * (self.length + self.width)

    def rec_sqr(self):
        return self.length * self.width

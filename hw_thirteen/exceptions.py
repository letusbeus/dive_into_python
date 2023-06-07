import view


class RectangleException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        raise NotImplementedError


class RectangleTypeError(RectangleException):
    def __str__(self):
        return view.is_number(self)


class RectangleValueError(RectangleException):
    def __str__(self):
        return view.is_positive(self)

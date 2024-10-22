class Punkt:
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @x.deleter
    def x(self):
        raise AttributeError('Nie można usunąć atrybutu x')

    @y.deleter
    def y(self):
        raise AttributeError('Nie można usunąć atrybutu y')

    def __repr__(self):
        return (f'{self.__module__}.'
                f'{self.__class__.__name__}'
                f'({self.x}, {self.y})')

    def __str__(self):
        return f'{self.x}, {self.y}'


class NazwanyPunkt(Punkt):
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        super().__init__(x, y)

from math import sqrt, pi


class Figure:
    def area_figure(self):
        raise NotImplementedError(
            'Не предопределен метод'
            'area_figure().')


class Circle(Figure):
    def __init__(self, radius):
        """
        :param radius: Радиус круга
        """
        self.radius = radius

        if not radius > 0:
            raise ValueError(
                'Ошибка введеных данных:'
                'Радиус не может быть <=0.')

    def area_figure(self):
        return pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        """
        :param side1: Первая сторона треугольника.
        :param side2: Вторая сторона треуголника.
        :param side3: Третья сторона треуголника.
        """
        self.a = side1
        self.b = side2
        self.c = side3

        if not (self.a > 0 and self.b > 0 and self.c > 0):
            raise ValueError(
                'Ошибка введенных данных:'
                'Стороны треугольника не могут быть <=0.')

        if not (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            raise ValueError(
                'Ошибка введенных данных:'
                'Фигура не является треуголником.')

    def area_figure(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def right_triangle(self):
        """ Проверка: является ли треугольник прямоугольным."""
        return (self.a ** 2 + self.b ** 2 == self.c ** 2 or
                self.a ** 2 + self.c ** 2 == self.b ** 2 or
                self.b ** 2 + self.c ** 2 == self.a ** 2)


class Rectangle(Figure):
    """Для добавления новой фигуры:
    создайте новый дочерний класс и
    определите для него метод"""
    def __init__(self, length, width):
        """
        :param length: Длина
        :param width: Ширина
        """
        raise NotImplementedError(
            'Фигура прямоуголник:'
            'не предусмотрена'
        )

    def area_figure(self):
        ...


def calculate_area(*args):
    if len(args) == 1:
        return Circle(*args).area_figure()
    elif len(args) == 2:
        return Rectangle(*args).area_figure()
    elif len(args) == 3:
        return Triangle(*args).area_figure()
    else:
        raise NotImplementedError(
            'Ошибка введеных данных:'
            'калькулятор поддерживает только'
            'круг и треугольник'
        )


if __name__ == '__main__':
    pass
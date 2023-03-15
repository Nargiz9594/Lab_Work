#Задание 1

from math import sqrt


class Circle:
    def __init__(self, a, b, r):
        self.r = r
        self.a = a
        self.b = b


def area(self):
    return math.pi * self.r ** 2

def perimeter(self):
    return 2 * math.pi * self.r

    def test_belongs(self, x, y):

        if (x - self.a) ** 2 + (y - self.b) ** 2 <= self.radius ** 2:
            return f'point A with coordinates {x, y} belongs to circle C with radius {self.radius}'
            return f'point A with coordinates {x, y} does not belong to circle C with radius {self.radius}'


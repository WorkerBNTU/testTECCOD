"""
3. Создать класс Point, который представляет собой точку
 в двумерном пространстве. Класс должен иметь методы для
  инициализации координат точки, вычисления расстояния до
   другой точки, а также для получения и изменения координат.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


c = Point(5, 6)
d = Point(3, 2)
print(c.distance(d))
c.x = 10
print(c)
print(c.distance(d))

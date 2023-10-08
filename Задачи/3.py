import math


class Shape:
    """Фигура"""
    def area(self) -> int | float:
        """Найти площадь"""
        pass


    def perimeter(self) -> int | float:
        """Найти периметр"""
        pass


class Circle(Shape):
    """Круг"""
    def __init__(self, radius):
        """Найти радиус"""
        self.radius=radius

    def area(self) -> int | float:
        area = math.pi * self.radius**2
        return area

    def perimeter(self) -> int | float:
        perimeter = 2 * math.pi * self.radius
        return perimeter


class Rectangle(Shape):
    """Прямоугольник"""
    def __init__(self, a: int | float, b:  int | float):
        """a, b - стороны прямоугольника"""
        self.a = a
        self.b = b

    def area(self) -> int | float:
        return self.a * self.b

    def perimeter(self) -> int | float:
        return (self.a + self.b) * 2


shape1=Circle(5)
shape2=Rectangle(3, 6.7)
print(f'Круг: площадь {shape1.area()}, длина окружности {shape1.perimeter()}')
print(f'Прямоугольник: площадь {shape2.area()}, периметр {shape2.perimeter()}')








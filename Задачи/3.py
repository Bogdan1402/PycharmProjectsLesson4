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


class Triangle(Shape):
    """Треугольник"""
    def __init__(self, a: int | float, b: int | float, c: int | float):
        """a,b,c - стороны треугольника"""
        self.a = a
        self.b = b
        self.c = c


    def area(self) -> int | float:
        p=(self.a + self.b + self.c)/2
        """s в квадрате"""
        s=p*(p-self.a)*(p-self.b)*(p-self.c)**0.5
        return s



    def perimeter(self) -> int | float:
        return self.a + self.b + self.c

    def is_equilateral(self) -> bool:
        """Является ли треугольник равносторонним"""
        if self.a == self.b == self.c:
            return True
        else:
            return False

    def is_isosceles(self) -> bool:
        """Является ли треугольник равнобедренным"""
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        else:
            return False




shape1=Circle(5)
shape2=Rectangle(3, 6.7)
print(f'Круг: площадь {shape1.area()}, длина окружности {shape1.perimeter()}')
print(f'Прямоугольник: площадь {shape2.area()}, периметр {shape2.perimeter()}')
shape3=Triangle(15, 30, 25.3)
print(f'Треугольник: площадь {shape3.area()}, периметр {shape3.perimeter()}')
print(f"Треугольник равносторонний: {shape3.is_equilateral()}, равнобедренный {shape3.is_isosceles()} ")






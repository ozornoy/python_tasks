class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculatePerimeter(self):
        return self.a + self.b + self.c

    def calculateArea(self):
        p = (self.a + self.b + self.c) / 2.0
        import math
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def printTriangleInfo(self):
        print(
            f"Стороны треугольника: a:{self.a}|b:{self.b}|c:{self.c}\n"
            f"Периметр треугольника: {self.calculatePerimeter()}\n"
            f"Площадь треугольника: {self.calculateArea()}"
        )


triangle = Triangle(10, 10, 15)
triangle.printTriangleInfo()

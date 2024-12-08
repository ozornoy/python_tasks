import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculateCircumference(self):
        return 2 * math.pi * self.radius

    def calculateArea(self):
        return math.pi * math.pow(self.radius, 2)

    def printCircleInfo(self):
        print(f"Круг:"
              f"Радиус = {self.radius}\n"
              f"Площадь = {self.calculateArea():.2f}\n"
              f"Длина окружности = {self.calculateCircumference():.2f}")


circle = Circle(10.0)
circle.printCircleInfo()

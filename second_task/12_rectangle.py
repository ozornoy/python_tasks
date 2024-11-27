class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height

    def calculatePerimeter(self):
        return (self.width + self.height) * 2

    def printRectangleInfo(self):
        print(f"Прямоугольник:\n"
              f"Ширина = {self.width}\n"
              f"Высота = {self.height}\n"
              f"Площадь = {self.calculateArea()}\n"
              f"Периметр = {self.calculatePerimeter()}")


rectangle = Rectangle(10, 10)
rectangle.printRectangleInfo()

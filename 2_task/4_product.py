class Product:
    def __init__(self, name, category, quantity, pricePerUnit):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.pricePerUnit = pricePerUnit

    def printProductInfo(self):
        print(
            f"Товар: {self.name},"
            f"Категория: {self.category},"
            f"Количество: {self.quantity},"
            f"Общая стоимость: {self.calculateTotalPrice()}"
        )

    def calculateTotalPrice(self):
        return self.quantity * self.pricePerUnit


product = Product("First Product", "Category", 10, 100)
product.quantity = 20

product.printProductInfo()

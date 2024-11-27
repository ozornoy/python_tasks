class Phone:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self._price = price

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def printPhoneDetails(self):
        print(f"Телефон: {self.brand} {self.model}, Цена: {self.price}")

    def applyDiscount(self, percentage):
        self.price = self.price - (self.price / 100 * percentage)


product = Phone("Iphone", "16 PRO", 500)
product.printPhoneDetails()
product.applyDiscount(50)
product.printPhoneDetails()

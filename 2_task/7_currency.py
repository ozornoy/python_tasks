class Currency:
    def __init__(self):
        self._name = ...
        self._rateToUSD = ...

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def rateToUSD(self):
        return self._rateToUSD

    @rateToUSD.setter
    def rateToUSD(self, value):
        self._rateToUSD = value

    def printProductInfo(self):
        print(f"Валюта: {self.name}, Курс к USD: {self.rateToUSD}")

    def convertToUSD(self, amount):
        return amount * self.rateToUSD


product = Currency()
product.name = "RUB"
product.rateToUSD = 90
product.printProductInfo()

print(f"Сумма в долларах: {product.convertToUSD(200)}")

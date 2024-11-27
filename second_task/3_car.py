class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = None

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def set_price(self, price):
        self.price = price

    def print_car_info(self):
        print(f"Бренд: {self.brand}, Модель: {self.model}, Год: {self.year}, Цена: {self.price}")


car = Car("Car brand", "Car model", "Car year")
car.set_price(2.34)

car.print_car_info()

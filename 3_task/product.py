from interfaces import IProduct


class Iphone(IProduct):
    def __init__(self, name: str, color: str, price: int, storage: int):
        super().__init__(name, "Iphone", color, price)
        self.storage = storage

    def get_description(self):
        return (
            f"Iphone {self.name}, Color: {self.color}, "
            f"Storage: {self.storage}GB, Price: ${self.price}"
        )


class ComputerMouse(IProduct):
    def __init__(self, name: str, color: str, price: int, dpi: int):
        super().__init__(name, "Computer Mouse", color, price)
        self.dpi = dpi

    def get_description(self):
        return (
            f"Mouse {self.name}, Color: {self.color}, "
            f"DPI: {self.dpi}, Price: ${self.price}"
        )

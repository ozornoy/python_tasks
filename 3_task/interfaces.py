from abc import ABC, abstractmethod
import uuid

from order import Order


class IProduct(ABC):
    def __init__(self, name: str, product_type: str, color: str, price: int):
        self.id = uuid.uuid4()
        self.name = name
        self.product_type = product_type
        self.color = color
        self.price = price

    @abstractmethod
    def get_description(self) -> str:
        pass


class IBasket(ABC):
    @abstractmethod
    def add_products(self, *products: IProduct) -> None:
        pass

    @abstractmethod
    def remove_product(self, product: IProduct) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass


class IOrders(ABC):
    @abstractmethod
    def create_order(self, basket: IBasket) -> Order:
        pass

    @abstractmethod
    def pay_for_order(self, order: Order) -> None:
        pass

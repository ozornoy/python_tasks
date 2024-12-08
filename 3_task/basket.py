import uuid
from typing import List

from third_task.product import Product


class Basket:
    def __init__(self):
        self.id = uuid.uuid4()
        self.products: List[Product] = []

from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name) -> None:
        for i in range(len(self.products)):
            if self.products[i].name == product_name:
                self.products.pop(i)
                return

    def __repr__(self):
        return "\n".join(f"{x.name}: {x.quantity}" for x in self.products)
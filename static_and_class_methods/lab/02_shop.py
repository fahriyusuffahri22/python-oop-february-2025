from __future__ import annotations
from typing import Dict

class Shop:
    SMALL_SHOP_CAPACITY = 10

    def __init__(self, name: str, _type: str, capacity: int):
        self.name = name
        self.type = _type
        self.capacity = capacity
        self.items: Dict[str, int] = {}

    @classmethod
    def small_shop(cls, name: str, _type: str) -> Shop:
        return cls(name, _type, cls.SMALL_SHOP_CAPACITY)

    def add_item(self, item_name: str) -> str:
        if self.capacity != sum(self.items.values()):
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the shop"

        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if not item_name in self.items or amount > self.items[item_name]:
           return f"Cannot remove {amount} {item_name}"

        if self.items[item_name] > amount:
            self.items[item_name] -= amount
        else:
            self.items.pop(item_name)

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
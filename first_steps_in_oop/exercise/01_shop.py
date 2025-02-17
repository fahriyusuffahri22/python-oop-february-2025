from typing import List

class Shop:
    def __init__(self, name: str, items: List[str]):
        self.name = name
        self.items = items

    def get_items_count(self) -> int:
        return len(self.items)
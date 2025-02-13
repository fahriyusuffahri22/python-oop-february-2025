class Glass:
    capacity: float = 250

    def __init__(self):
        self.content: float = 0

    def fill(self, ml: float) -> str:
        if Glass.capacity - self.content >= ml:
            self.content += ml
            return f"Glass filled with {ml} ml"

        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        return f"{Glass.capacity - self.content} ml left"
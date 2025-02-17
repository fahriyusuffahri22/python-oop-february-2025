class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int) -> None:
        if self.status() >= quantity:
            self.quantity += quantity

    def status(self) -> int:
        return self.size - self.quantity
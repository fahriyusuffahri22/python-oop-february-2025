class Hero:
    def __init__(self, name: str, health: float):
        self.name = name
        self.health = health

    def defend(self, damage: float) -> None | str:
        self.health = max(self.health - damage, 0)

        if self.health == 0:
            return f"{self.name} was defeated"

    def heal(self, amount: float) -> None:
        self.health += amount
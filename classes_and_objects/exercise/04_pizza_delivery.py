from typing import Dict

class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: Dict[str, int]):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered: bool = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> None | str:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> None | str:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self) -> str:
        self.ordered = True

        return (
            f"You've ordered pizza {self.name} prepared with "
            f"{', '.join(f'{k}: {v}' for k, v in self.ingredients.items())} and the price will be {self.price}lv."
        )
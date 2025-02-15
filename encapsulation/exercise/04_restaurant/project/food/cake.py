from project.food.dessert import Dessert


class Cake(Dessert):
    PRICE: float = 5
    GRAMS: float = 250
    CALORIES: float = 1000

    def __init__(self, name: str):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
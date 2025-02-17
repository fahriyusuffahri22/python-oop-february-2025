from typing import List, Type

from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    @property
    def _sound(self) -> str:
        return "Squeak"

    @property
    def _food_types(self) -> List[Type[Food]]:
        return [Vegetable, Fruit]

    @property
    def _food_weight(self) -> float:
        return 0.1


class Dog(Mammal):
    @property
    def _sound(self) -> str:
        return "Woof!"

    @property
    def _food_types(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def _food_weight(self) -> float:
        return 0.4



class Cat(Mammal):
    @property
    def _sound(self) -> str:
        return "Meow"

    @property
    def _food_types(self) -> List[Type[Food]]:
        return [Vegetable, Meat]

    @property
    def _food_weight(self) -> float:
        return 0.3


class Tiger(Mammal):
    @property
    def _sound(self) -> str:
        return "ROAR!!!"

    @property
    def _food_types(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def _food_weight(self) -> float:
        return 1
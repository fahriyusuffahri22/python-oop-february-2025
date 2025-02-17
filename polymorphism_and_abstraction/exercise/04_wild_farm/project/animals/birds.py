from typing import List, Type

from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    @property
    def _sound(self) -> str:
        return "Hoot Hoot"

    @property
    def _food_types(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def _food_weight(self) -> float:
        return 0.25



class Hen(Bird):
    @property
    def _sound(self) -> str:
        return "Cluck"

    @property
    def _food_types(self) -> List[Type[Food]]:
        return Food.__subclasses__()

    @property
    def _food_weight(self) -> float:
        return 0.35
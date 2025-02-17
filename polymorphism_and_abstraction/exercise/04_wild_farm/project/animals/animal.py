from abc import ABC, abstractmethod
from typing import List, Type
from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @property
    @abstractmethod
    def _sound(self) -> str:
        ...

    @property
    @abstractmethod
    def _food_types(self) -> List[Type[Food]]:
        ...

    @property
    @abstractmethod
    def _food_weight(self) -> float:
        ...

    def make_sound(self) -> str:
        return self._sound

    def feed(self, food: Food) -> None | str:
        if food.__class__ not in self._food_types:
            return  f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self._food_weight * food.quantity


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
from abc import ABC, abstractmethod
from typing import Tuple, Dict


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def _expenses(self) -> int:
        ...

    @property
    @abstractmethod
    def _sponsors(self) -> Tuple[Dict[int, int], ...]:
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value: int):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = self._expenses

        for sponsor in self._sponsors:
            for position in sponsor:
                if position >= race_pos:
                    revenue += sponsor[position]
                    break

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
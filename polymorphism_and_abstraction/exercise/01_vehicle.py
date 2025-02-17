from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption : int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        fuel_needed = (self.fuel_consumption + self.air_conditioners_fuel_consumption) * distance

        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    @property
    @abstractmethod
    def air_conditioners_fuel_consumption(self) -> float:
        ...

    @abstractmethod
    def refuel(self, fuel: int) -> float:
        ...


class Car(Vehicle):
    @property
    def air_conditioners_fuel_consumption(self) -> float:
        return 0.9

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel

class Truck (Vehicle):
    FUEL_REMAINING_PERCENTAGE: float = 0.95

    @property
    def air_conditioners_fuel_consumption(self) -> float:
        return 1.6

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * self.FUEL_REMAINING_PERCENTAGE
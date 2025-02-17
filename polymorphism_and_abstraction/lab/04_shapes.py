from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_area(self) -> float:
        return pi * self.__radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def calculate_area(self) -> int:
        return self.__width * self.__height

    def calculate_perimeter(self) -> int:
        return 2 * (self.__width + self.__height)
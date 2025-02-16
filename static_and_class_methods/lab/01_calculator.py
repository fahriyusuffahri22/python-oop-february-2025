from functools import reduce


class Calculator:
    @staticmethod
    def add(*args) -> int | float:
        return sum(args)

    @staticmethod
    def multiply(*args) -> int | float:
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args) -> int | float:
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args) -> int | float:
        return reduce(lambda x, y: x - y, args)
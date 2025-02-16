from __future__ import annotations

import math


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> Integer | str:
        if isinstance(float_value, float):
            return cls(math.floor(float_value))

        return "value is not a float"

    @classmethod
    def from_roman(cls, value: str) -> Integer:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        nums = [roman_numerals[x] for x in value]
        return cls(sum(nums[i] if nums[i] > nums[i + 1] else -nums[i] for i in range(len(nums) - 1)) + nums[-1])

    @classmethod
    def from_string(cls, value: str) -> Integer | str:
        if isinstance(value, str) and value.isdigit():
            return cls(int(value))

        return "wrong type"
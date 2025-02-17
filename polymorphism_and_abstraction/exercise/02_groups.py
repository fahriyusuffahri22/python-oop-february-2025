from __future__ import annotations
from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other: Person):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other: Group):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"

    def __iter__(self):
        for i in range(len(self)):
            yield f"Person {i}: {self.people[i]}"

    def __getitem__(self, index: int):
        return f"Person {index}: {self.people[index]}"
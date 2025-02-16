from __future__ import annotations
from calendar import month_name

class DVD:
    IS_RENTED_DEFAULT: bool = False

    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = DVD.IS_RENTED_DEFAULT

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int) -> DVD:
        _, month, year = (int(x) for x in date.split("."))
        return cls(name, _id, year, month_name[month], age_restriction)

    def __repr__(self):
        return (
            f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction "
            f"{self.age_restriction}. Status: {'' if self.is_rented else 'not '}rented"
        )
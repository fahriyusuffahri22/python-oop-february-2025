from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity()-> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def get_customer(self, customer_id: int) -> Customer:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.get_customer(customer_id)

        for dvd in customer.rented_dvds:
            if dvd.id == dvd_id:
                return f"{customer.name} has already rented {dvd.name}"

        for i in range(len(self.dvds)):
            if self.dvds[i].id == dvd_id:
                if customer.age < self.dvds[i].age_restriction:
                    return f"{customer.name} should be at least {self.dvds[i].age_restriction} to rent this movie"

                dvd = self.dvds.pop(i)
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                return f"{customer.name} has successfully rented {dvd.name}"

        return "DVD is already rented"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.get_customer(customer_id)

        for i in range(len(customer.rented_dvds)):
            if customer.rented_dvds[i].id == dvd_id:
                dvd = customer.rented_dvds.pop(i)
                dvd.is_rented = False
                self.dvds.append(dvd)
                return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return "\n".join([
            *(str(x) for x in self.customers),
            *(str(x) for y in self.customers for x in y.rented_dvds)
        ])
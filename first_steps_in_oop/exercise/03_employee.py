class Employee:
    def __init__(self, _id: float, first_name: str, last_name: str, salary: float):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self) -> float:
       return self.salary * 12

    def raise_salary(self, amount: float) -> float:
        self.salary += amount
        return self.salary
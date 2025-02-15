from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if price > self.__budget:
            return "Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) != self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name) -> str:
        for i in range(len(self.workers)):
            if self.workers[i].name == worker_name:
                self.workers.pop(i)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salary_sum = sum(x.salary for x in self.workers)

        if self.__budget >= salary_sum:
            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        money_for_care_sum = sum(x.money_for_care for x in self.animals)

        if self.__budget >= money_for_care_sum:
            self.__budget -= money_for_care_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        animals = {x.__name__: [] for x in Animal.__subclasses__()}
        data = [f"You have {len(self.animals)} animals"]

        for animal in self.animals:
            animals[animal.__class__.__name__].append(animal)

        for class_name in ("Lion", "Tiger", "Cheetah"):
            data.append(f"----- {len(animals[class_name])} {class_name}s:")
            data.extend(str(x) for x in animals[class_name])

        return "\n".join(data)

    def workers_status(self) -> str:
        data = [f"You have {len(self.workers)} workers"]
        workers = {x.__name__: [] for x in Worker.__subclasses__()}

        for worker in self.workers:
            workers[worker.__class__.__name__].append(worker)

        for class_name in ("Keeper", "Caretaker", "Vet"):
            data.append(f"----- {len(workers[class_name])} {class_name}s:")
            data.extend(str(x) for x in workers[class_name])

        return "\n".join(data)
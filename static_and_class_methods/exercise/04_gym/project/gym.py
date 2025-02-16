from typing import List, Any
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def get(collection: List[Any], _id: int) -> Any:
        for x in collection:
            if x.id == _id:
                return x

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = self.get(self.subscriptions, subscription_id)
        customer = self.get(self.customers, subscription.customer_id)
        trainer = self.get(self.trainers, subscription.trainer_id)
        plan = self.get(self.plans, subscription.exercise_id)
        equipment = self.get(self.equipment, plan.equipment_id)

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
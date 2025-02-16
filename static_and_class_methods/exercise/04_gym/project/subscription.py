from project.autoincremented_id_mixin import AutoincrementedIdMixin


class Subscription(AutoincrementedIdMixin):
    id: int = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        super().__init__()
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
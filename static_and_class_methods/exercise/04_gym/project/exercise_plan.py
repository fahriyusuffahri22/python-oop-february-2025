from __future__ import annotations
from project.autoincremented_id_mixin import AutoincrementedIdMixin


class ExercisePlan(AutoincrementedIdMixin):
    id: int = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        super().__init__()
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int) -> ExercisePlan:
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
from project.autoincremented_id_mixin import AutoincrementedIdMixin



class Equipment(AutoincrementedIdMixin):
    id: int = 1

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
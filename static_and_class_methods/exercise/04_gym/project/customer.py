from project.autoincremented_id_mixin import AutoincrementedIdMixin



class Customer(AutoincrementedIdMixin):
    id: int = 1

    def __init__(self, name: str, address: str, email: str):
        super().__init__()
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
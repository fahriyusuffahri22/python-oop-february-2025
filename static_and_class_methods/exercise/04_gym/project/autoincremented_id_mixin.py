class AutoincrementedIdMixin:
    id = 1

    def __init__(self):
        self.id = self.get_next_id()
        self.__class__.id += 1

    @classmethod
    def get_next_id(cls) -> int:
        return cls.id
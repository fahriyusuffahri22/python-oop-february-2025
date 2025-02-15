class Mammal:
    __kingdom: str = "animals"

    def __init__(self, name: str, _type: str, sound: str):
        self.name = name
        self.type = _type
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    @classmethod
    def get_kingdom(cls) -> str:
        return cls.__kingdom

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"
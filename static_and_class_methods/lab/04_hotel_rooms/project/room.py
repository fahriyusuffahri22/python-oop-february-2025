class Room:
    GUESTS_DEFAULT: int = 0
    IS_TAKEN_DEFAULT: bool = False

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = Room.GUESTS_DEFAULT
        self.is_taken = Room.IS_TAKEN_DEFAULT

    def take_room(self, people) -> None | str:
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests = people

    def free_room(self) -> None | str:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0
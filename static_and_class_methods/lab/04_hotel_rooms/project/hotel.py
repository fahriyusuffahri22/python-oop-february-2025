from __future__ import annotations
from typing import List
from project.room import Room


class Hotel:
    ROOMS_DEFAULT: List[Room] = []
    GUESTS_DEFAULT: int = 0

    def __init__(self, name: str):
        self.name = name
        self.rooms = Hotel.ROOMS_DEFAULT
        self.guests = Hotel.GUESTS_DEFAULT

    @classmethod
    def from_stars(cls, stars_count: int) -> Hotel:
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> None:
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
                self.guests += room.guests
                return

    def free_room(self, room_number) -> None:
        for room in self.rooms:
            if room.number == room_number:
                guests = room.guests

                if room.free_room() is None:
                    self.guests -= guests

                return

    def status(self) -> str:
        free_rooms_numbers = []
        taken_rooms_numbers = []

        for room in self.rooms:
            if room.is_taken:
                taken_rooms_numbers.append(str(room.number))
            else:
                free_rooms_numbers.append(str(room.number))

        return (
            f"Hotel {self.name} has {self.guests} total guests\n"
            f"Free rooms: {', '.join(free_rooms_numbers)}\n"
            f"Taken rooms: {', '.join(taken_rooms_numbers)}"
        )
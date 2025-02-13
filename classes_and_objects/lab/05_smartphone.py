from typing import List


class Smartphone:
    def __init__(self, memory: float):
        self.memory = memory
        self.apps: List[str] = []
        self.is_on: bool = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: float) -> str:
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        if app_memory > self.memory:
            return f"Not enough memory to install {app}"

        self.memory -= app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
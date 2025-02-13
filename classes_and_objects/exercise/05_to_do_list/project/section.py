from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        total_tasks = len(self.tasks)
        self.tasks = [x for x in self.tasks if not x.completed]
        return  f"Cleared {total_tasks - len(self.tasks)} tasks."

    def view_section(self) -> str:
        return  "\n".join([
            f"Section {self.name}:",
            *(x.details() for x in self.tasks)
        ])
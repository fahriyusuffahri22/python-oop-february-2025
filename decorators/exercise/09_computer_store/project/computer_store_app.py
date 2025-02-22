from  project.computer_types.desktop_computer import DesktopComputer
from  project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        computer_types = {
            "Desktop Computer": DesktopComputer,
            "Laptop": Laptop
        }

        if type_computer in computer_types:
            self.warehouse.append(computer_types[type_computer](manufacturer, model))
            return self.warehouse[-1].configure_computer(processor, ram)

        raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for i in range(len(self.warehouse)):
            if self.__meets_requirements(self.warehouse[i], client_budget, wanted_processor, wanted_ram):
                computer = self.warehouse.pop(i)
                self.profits += client_budget - computer.price

                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")

    @staticmethod
    def __meets_requirements(computer, client_budget, wanted_processor, wanted_ram):
        if computer.price > client_budget:
            return False
        if computer.processor != wanted_processor:
            return False
        if computer.ram < wanted_ram:
            return False

        return True

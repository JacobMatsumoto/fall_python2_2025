from abc import ABC, abstractmethod


class Tea(ABC):
    def __init__(self, size, tea_type,):
        self.size = size
        self.tea_type = tea_type


    @abstractmethod
    def add_in(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def description(self):
        pass


class Matcha(Tea):
    def __init__(self, size, tea_type,):
        super().__init__(size, tea_type,)

    def add_in(self):
        return "Almond milk"

    def price(self):
        return "$4-$7.50"

    def description(self):
        return f"Matcha: {self.size}, {self.tea_type}, with {self.add_in()} is priced at {self.price()} depending on size"
    

class GreenTea(Tea):
    def __init__(self, size, tea_type,):
        super().__init__(size, tea_type,)

    def add_in(self):
        return "Whole Milk"

    def price(self):
        return "$2.50-$4.50"

    def description(self):
        return f"GreenTea: {self.size}, {self.tea_type}, with {self.add_in()} is priced at {self.price()} depending on size"

iced_matcha = Matcha("Large", "Matcha")
print(iced_matcha.description())

hot_green_tea = GreenTea("Small", "Green Tea")
print(hot_green_tea.description())
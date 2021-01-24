from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, rate):
        self.size = rate
        self.growth = rate

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        volume = (self.size / 6.5 + 0.5)
        return volume


class Costume(Clothes):
    @property
    def calculate(self):
        volume = (2 * self.growth + 0.3)
        return volume


grey_coat = Clothes(3)
print(grey_coat.calculate)
small_costume = Clothes(4)
print(small_costume.calculate)

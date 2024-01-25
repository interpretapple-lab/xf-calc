from abc import ABC, abstractmethod


class FuzzyNumber(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def addition(self, FuzzyNumber):
        pass

    @abstractmethod
    def subtraction(self, FuzzyNumber):
        pass

    @abstractmethod
    def multiplication(self, FuzzyNumber):
        pass

    @abstractmethod
    def output(self):
        pass

    @abstractmethod
    def representation(self):
        pass

    @abstractmethod
    def toCartesian(self):
        pass
